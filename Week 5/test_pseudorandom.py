import unittest
from pseudorandom import pseudo_random


class TestRandom(unittest.TestCase):
    def test_pseudo_random(self):
        """
        Tests that the pseudo-random function:
        - Returns same values on same seed
        - Returns different values with different seed
        - Returns `n` elements when `n` elements are asked
        - Returns all values between 0 and 1
        - Returns all unique values
        """
        seed = 125235
        seed2 = 109249814
        
        n = 12

        x1 = pseudo_random(seed, n=n)
        x2 = pseudo_random(seed, n=n)
        x3 = pseudo_random(seed2, n=n)

        clauses = [
            x1 == x2,
            x1 != x3,
            len(x1) == n,
            all([0 < x < 1 for x in x1]),
            len(set(x1)) == len(x1) 
        ]

        for clause in clauses:
            self.assertTrue(clause)

if __name__ == '__main__':
    unittest.main()
