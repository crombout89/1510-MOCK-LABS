import unittest
from time_intervals import merge_intervals

class TestMergeIntervals(unittest.TestCase):
    def test_merge_with_overlaps(self):
        intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
        self.assertEqual(merge_intervals(intervals), [(1, 6), (8, 10), (15, 18)])

    def test_merge_with_adjacent_intervals(self):
        intervals = [(1, 4), (4, 5)]
        self.assertEqual(merge_intervals(intervals), [(1, 5)])

    def test_no_overlapping_intervals(self):
        intervals = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(merge_intervals(intervals), [(1, 2), (3, 4), (5, 6)])

    def test_single_interval(self):
        intervals = [(1, 10)]
        self.assertEqual(merge_intervals(intervals), [(1, 10)])

    def test_empty_list(self):
        intervals = []
        self.assertEqual(merge_intervals(intervals), [])

    def test_large_overlapping_intervals(self):
        intervals = [(1, 10), (2, 5), (6, 12)]
        self.assertEqual(merge_intervals(intervals), [(1, 12)])

if __name__ == "__main__":
    unittest.main()