import unittest
from voting_system import analyze_votes

class TestAnalyzeVotes(unittest.TestCase):
    """
    Unit test suite for the analyze_votes function.
    """

    def test_all_registered_voters_voted(self):
        """
        Test case where all registered voters voted and no unregistered voters tried to vote.
        """
        test_registered_voters = {"voter1", "voter2", "voter3"}
        test_votes_cast = {"voter1", "voter2", "voter3"}
        result = analyze_votes(test_registered_voters, test_votes_cast)
        self.assertEqual(result, {"voted_count": 3, "non_voters_count": 0, "unregistered_voters_count": 0})

    def test_no_registered_voters_voted(self):
        """
        Test case where none of the registered voters voted, and all votes were from unregistered voters.
        """
        test_registered_voters = {"voter1", "voter2", "voter3"}
        test_votes_cast = {"voter4", "voter5", "voter6"}
        result = analyze_votes(test_registered_voters, test_votes_cast)
        self.assertEqual(result, {"voted_count": 0, "non_voters_count": 3, "unregistered_voters_count": 3})

    def test_some_registered_voters_and_some_unregistered_voters(self):
        """
        Test case where some registered voters voted and some unregistered voters also voted.
        """
        test_registered_voters = {"voter1", "voter2", "voter3"}
        test_votes_cast = {"voter1", "voter2", "voter4", "voter5"}
        result = analyze_votes(test_registered_voters, test_votes_cast)
        self.assertEqual(result, {"voted_count": 2, "non_voters_count": 1, "unregistered_voters_count": 2})

    def test_empty_registered_voters(self):
        """
        Test case where there are no registered voters, but some votes are cast.
        """
        test_registered_voters = set()
        test_votes_cast = {"voter1", "voter2"}
        result = analyze_votes(test_registered_voters, test_votes_cast)
        self.assertEqual(result, {"voted_count": 0, "non_voters_count": 0, "unregistered_voters_count": 2})

    def test_empty_votes_cast(self):
        """
        Test case where no votes are cast, but there are registered voters.
        """
        test_registered_voters = {"voter1", "voter2"}
        test_votes_cast = set()
        result = analyze_votes(test_registered_voters, test_votes_cast)
        self.assertEqual(result, {"voted_count": 0, "non_voters_count": 2, "unregistered_voters_count": 0})

    def test_invalid_inputs(self):
        """
        Test case to ensure the function raises a TypeError for invalid inputs.
        """
        with self.assertRaises(TypeError):
            analyze_votes(["voter1", "voter2"], {"voter1"})  # Invalid registered_voters type

        with self.assertRaises(TypeError):
            analyze_votes({"voter1", "voter2"}, ["voter1"])  # Invalid votes_cast type

# Run the unit tests
if __name__ == "__main__":
    unittest.main(verbosity=2)