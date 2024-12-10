import unittest
from sparsevector import sparse_add


class TestSparseAdd(unittest.TestCase):
    def test_add_normal(self):
        # Test adding two normal sparse vectors
        vector_a = {"length": 3, 0: 1, 2: 3}
        vector_b = {"length": 3, 0: 4, 1: 5, 2: 6}
        expected = {"length": 3, 0: 5, 1: 5, 2: 9}
        self.assertEqual(sparse_add(vector_a, vector_b), expected)

    def test_add_no_overlap(self):
        # Test adding two vectors with no overlap in indices
        vector_a = {"length": 3, 0: 1}
        vector_b = {"length": 3, 1: 2}
        expected = {"length": 3, 0: 1, 1: 2}
        self.assertEqual(sparse_add(vector_a, vector_b), expected)

    def test_add_empty_vectors(self):
        # Test adding two empty sparse vectors
        vector_a = {"length": 3}
        vector_b = {"length": 3}
        expected = {"length": 3}
        self.assertEqual(sparse_add(vector_a, vector_b), expected)

    def test_add_error_different_lengths(self):
        # Test adding two vectors with different lengths
        vector_a = {"length": 3, 0: 1}
        vector_b = {"length": 4, 1: 2}
        with self.assertRaises(ValueError):
            sparse_add(vector_a, vector_b)


if __name__ == '__main__':
    unittest.main()