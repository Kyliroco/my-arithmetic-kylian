import unittest
from my_arithmetic_kylian.pgcd import pgcd


class TestPGCD(unittest.TestCase):
    def test_pgcd(self):
        self.assertEqual(pgcd(48, 18), 6)


if __name__ == "__main__":
    unittest.main()
