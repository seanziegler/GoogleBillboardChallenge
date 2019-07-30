import unittest
from basicPrime import basicPrime

class TestPrimeMethods(unittest.TestCase):



    def test_basicPrimesWithComposities(self):
        firstComposites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36]
        for composite in firstComposites:
            self.assertFalse(basicPrime(composite))

    def test_basicPrimesWithNegativeZeroOne(self):
        with self.assertRaises(ValueError):
            basicPrime(-1)
        with self.assertRaises(ValueError):
            basicPrime(0)
        with self.assertRaises(ValueError):
            basicPrime(2)

    def test_basicPrimeWithString(self):
        with self.assertRaises(TypeError):
            basicPrime('test')

    def test_basicPrimeWithPrimes(self):
        firstPrimes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for prime in firstPrimes:
            self.assertTrue(basicPrime(prime))


if __name__ == '__main__':
    unittest.main()
