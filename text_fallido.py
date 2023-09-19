import unittest


class Test(unittest.TestCase):
    def test_run(self):
        expected = 42
        actual = 42
        self.assertEqual(expected, actual)