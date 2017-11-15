import unittest
try:
    import unittest.mock as mock
except ImportError:
    import mock
import sys
import wsl_path_exe


class Testslib(unittest.TestCase):
    def test_wsl_running(self):
        self.assertTrue(wsl_path_exe.wsl_running())

    @mock.patch('platform.platform')
    def test_wsl_running_false(self, platform_mock):
        platform_mock.return_value = 'X-4.4.0-43-Y-x86_64-Z'
        self.assertFalse(wsl_path_exe.wsl_running())

    def test_list_paths(self):
        self.assertTrue(isinstance(wsl_path_exe.list_paths(), list))

    @mock.patch('os.getenv')
    def test_list_paths_empty(self, path_empty_mock):
        path_empty_mock.return_value = ''
        self.assertIsInstance(wsl_path_exe.list_paths(), list)


if __name__ == '__main__':
    unittest.main()
