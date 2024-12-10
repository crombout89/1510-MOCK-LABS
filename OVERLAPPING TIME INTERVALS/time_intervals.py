from typing import *

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping time intervals.

    :param intervals: A list of tuples, where each tuple represents a time interval (start, end).
    :precondition: intervals must be a list of tuples that contain integers.
    :postcondition: Returns a list of tuples containing the merged intervals.
    :return: A list of tuples, where each tuple represents a merged time interval (start, end).

    >>> test_intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    >>> merge_intervals(test_intervals)
    [(1, 6), (8, 10), (15, 18)]

    >>> test_intervals = [(1, 4), (4, 5)]
    >>> merge_intervals(test_intervals)
    [(1, 5)]
    """
    # Step 1: Handle the edge case where the input list is empty
    # If there are no intervals, there is nothing to merge, so return an empty list.
    if not intervals:
        return []

    # Step 2: Sort intervals by their start time
    # Sorting ensures that we process intervals in the order of their start times.
    # This makes it easier to compare adjacent intervals and detect overlaps.
    # For example, intervals [(8, 10), (1, 3), (2, 6)] will be sorted to [(1, 3), (2, 6), (8, 10)].
    intervals.sort(key=lambda x: x[0])

    # Step 3: Initialize the list of merged intervals
    # Start by adding the first interval from the sorted list to the merged_intervals list.
    # This serves as the "base" interval that we will compare others against.
    merged_intervals = [intervals[0]]

    # Step 4: Iterate through the rest of the intervals
    # We start from the second interval (intervals[1:]) since the first one is already in merged_intervals.
    for current_start, current_end in intervals[1:]:
        # Step 4.1: Retrieve the last interval from the merged_intervals list
        # This is the interval we will compare the current interval to.
        last_start, last_end = merged_intervals[-1]

        # Step 4.2: Check if the current interval overlaps with the last merged interval
        # Two intervals overlap if the start time of the current interval is less than or equal
        # to the end time of the last merged interval.
        if current_start <= last_end:
            # Step 4.3: If they overlap, merge the intervals
            # To merge, we update the end time of the last interval in merged_intervals
            # to the maximum of its current end time and the end time of the current interval.
            # This ensures that the resulting interval covers the entire overlapping range.
            merged_intervals[-1] = (last_start, max(last_end, current_end))
        else:
            # Step 4.4: If they do not overlap, add the current interval as-is
            # Since the intervals are sorted, we know that the current interval starts
            # after the end of the last merged interval, so we can safely add it to the list.
            merged_intervals.append((current_start, current_end))

    # Step 5: Return the merged intervals
    # After processing all intervals, the merged_intervals list will contain the final result,
    # where all overlapping intervals have been merged.
    return merged_intervals

def main():
    """ Drive the program. """

    print("Example 1:")
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    print(f"Original intervals: {intervals}")
    print(f"Merged intervals: {merge_intervals(intervals)}")

    print("\nExample 2:")
    intervals = [(1, 4), (4, 5)]
    print(f"Original intervals: {intervals}")
    print(f"Merged intervals: {merge_intervals(intervals)}")

    print("\nExample 3:")
    intervals = [(1, 2), (3, 4), (5, 6)]
    print(f"Original intervals: {intervals}")
    print(f"Merged intervals: {merge_intervals(intervals)}")

if __name__ == "__main__":
    main()