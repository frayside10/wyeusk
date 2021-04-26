import unittest

class CheckImport(unittest.TestCase):
    def setUp(self) -> None:
        self.listing = ['A']
        self.listing2 = ['A']

    def test_import_returns(self):
        self.assertEqual(1, 1.0)

    def test_data_vol(self):
        self.assertEqual(100, 100.00)

    def test_failed(self):
        with self.assertRaises(ZeroDivisionError):
            1/0

    def test_not_location(self):
        self.assertListEqual(self.listing, self.listing2)

if __name__ == "__main__":
    unittest.main()
