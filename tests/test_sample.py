import unittest

class TestSample(unittest.TestCase):
    def test_samples(self):
        self.assertEqual(42,42)

    def test_samples_wrong(self):
        self.assertEqual(42,0)
