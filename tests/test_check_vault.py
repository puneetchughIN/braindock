"""Behavior checks against real temporary vaults; no third-party packages."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_vault.py'
HEADER = '---\ntype: note\ntags: []\nupdated: 2026-09-23\n---\n\n'

class VaultChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('README.md', 'Start Here.md', 'AGENTS.md', 'VAULT-SPEC.md', 'SECURITY.md', 'Projects/00 Projects.md'):
            self.write(name)

    def write(self, name, body='', header=HEADER):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(header + body)
        return path

    def run_check(self):
        return subprocess.run([sys.executable, str(SCRIPT), str(self.root)], text=True, capture_output=True)

    def assert_issue(self, marker):
        result = self.run_check()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(marker, result.stdout)
        return result

    def test_valid_vault_is_read_only_and_portable(self):
        self.write('Knowledge/A Note.md', '[home](../Start%20Here.md) [[README|Overview]]')
        self.write('README.md', '[note](Knowledge/A%20Note.md#heading) ![asset](assets/picture.svg)')
        self.write('assets/picture.svg', '<svg/>', header='')
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_missing_root_record_fails(self):
        (self.root / 'Start Here.md').unlink()
        self.assert_issue('required')

    def test_empty_metadata_fails(self):
        self.write('Bad.md', header='---\ntype:\ntags: []\nupdated: invalid\n---\n')
        self.assert_issue('metadata')

    def test_duplicate_names_case_insensitive_fail(self):
        self.write('A/Topic.md')
        self.write('B/topic.md')
        self.assert_issue('duplicate')

    def test_broken_markdown_and_wikilinks_fail(self):
        for link in ('[missing](Missing.md)', '[[Missing|alias]]', '![[Missing.png]]'):
            with self.subTest(link=link):
                self.write('README.md', link)
                self.assert_issue('broken link')

    def test_working_placeholders_fail_even_if_type_is_template(self):
        self.write('Projects/Example.md', '{{project}}', header=HEADER.replace('type: note','type: template'))
        self.assert_issue('placeholder')

    def test_templates_and_code_examples_are_exempt(self):
        self.write('Templates/Blank.md', '{{project}} [future]({{project_url}}%20Brief.md)')
        self.write('README.md', '`{{example}}`\n```md\n[example](Missing.md)\n```\n~~~md\n[[Missing]]\n~~~\n[web](https://example.com) [email](mailto:hello@example.com)')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_absolute_paths_fail_including_inside_code(self):
        for value in ('`/Users/example/Documents/vault`', '`/home/example/vault`', 'C:\\Users\\example\\vault'):
            with self.subTest(value=value):
                self.write('README.md', value)
                self.assert_issue('machine path')

    def test_relative_escape_fails_even_if_target_exists(self):
        outside = self.root.parent / (self.root.name + '-outside.md')
        outside.write_text('outside')
        self.addCleanup(outside.unlink)
        self.write('README.md', f'[outside](../{outside.name})')
        self.assert_issue('outside vault')

    def test_symlinks_are_reported_and_not_read(self):
        outside = self.root.parent / (self.root.name + '-private.md')
        outside.write_text('PRIVATE SENTINEL')
        self.addCleanup(outside.unlink)
        (self.root / 'Linked.md').symlink_to(outside)
        result = self.assert_issue('symlink')
        self.assertNotIn('PRIVATE SENTINEL', result.stdout)

    def test_symlinked_root_is_rejected(self):
        link = self.root.parent / (self.root.name + '-link')
        link.symlink_to(self.root, target_is_directory=True)
        self.addCleanup(link.unlink)
        result = subprocess.run([sys.executable, str(SCRIPT), str(link)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('symlink', result.stdout)

    def test_nested_repository_is_reported_and_skipped(self):
        self.write('Product/.git', 'gitdir: elsewhere', header='')
        self.write('Product/Invalid.md', header='')
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn('nested repository', result.stdout)
        self.assertNotIn('Invalid.md', result.stdout)

    def test_angle_links_and_wikilink_relative_paths(self):
        self.write('Knowledge/First.md', '[other](<Second Note.md>) [[../README|home]]')
        self.write('Knowledge/Second Note.md')
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

if __name__ == '__main__':
    unittest.main()
