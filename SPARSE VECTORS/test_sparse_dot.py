import unittest
from sparsevector import sparse_dot_product


class TestSparseDotProduct(unittest.TestCase):
    def test_dot_normal(self):
        # Test dot product of two normal sparse vectors
        vector_a = {"length": 3, 0: 1, 2: 3}
        vector_b = {"length": 3, 0: 4, 1: 5, 2: 6}
        expected = 22  # (1 * 4) + (3 * 6) = 22
        self.assertEqual(sparse_dot_product(vector_a, vector_b), expected)

    def test_dot_no_overlap(self):
        # Test dot product of two vectors with no overlapping indices
        vector_a = {"length": 3, 0: 1}
        vector_b = {"length": 3, 1: 2}
        expected = 0  # No overlapping indices, so result is 0
        self.assertEqual(sparse_dot_product(vector_a, vector_b), expected)

    def test_dot_empty_vectors(self):
        # Test dot product of two empty sparse vectors
        vector_a = {"length": 3}
        vector_b = {"length": 3}
        expected = 0  # No elements to multiply
        self.assertEqual(sparse_dot_product(vector_a, vector_b), expected)

    def test_dot_error_different_lengths(self):
        # Test dot product of two vectors with different lengths
        vector_a = {"length": 3, 0: 1}
        vector_b = {"length": 4, 1: 2}
        with self.assertRaises(ValueError):
            sparse_dot_product(vector_a, vector_b)


if __name__ == '__main__':
    unittest.main()