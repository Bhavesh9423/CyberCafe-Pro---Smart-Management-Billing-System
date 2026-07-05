import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import app as app_module


class ScannerFlowTests(unittest.TestCase):
    def test_get_scanner_path_uses_environment_override(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            os.environ['SCANNER_PATH'] = tmpdir
            self.assertEqual(app_module.get_scanner_path(), tmpdir)
            os.environ.pop('SCANNER_PATH', None)

    def test_get_latest_scanned_file_returns_newest_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            older = os.path.join(tmpdir, 'old.pdf')
            newer = os.path.join(tmpdir, 'new.pdf')
            with open(older, 'wb') as fh:
                fh.write(b'old')
            with open(newer, 'wb') as fh:
                fh.write(b'newer')
            os.utime(older, (1, 1))
            os.utime(newer, (2, 2))
            self.assertEqual(app_module.get_latest_scanned_file(tmpdir), newer)


if __name__ == '__main__':
    unittest.main(verbosity=2)
