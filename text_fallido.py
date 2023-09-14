import unittest


class Test(unittest.TestCase):
    def test_run(self):
        expected = 42
        actual = 314
        self.assertEqual(expected, actual)