from typing import *

def analyze_votes(registered_voters: Set[str], votes_cast: Set[str]) -> Dict[str, int]:
    """
    Analyze voting results by determining how many registered voters actually voted, how many registered voters did
    not vote, and how many unregistered voters tried to vote.

    :param registered_voters: A set of registered voter IDs (strings).
    :param votes_cast: A set of IDs (strings) of people who cast votes.
    :precondition: registered_voters must be a non-empty set of strings.
    :precondition: votes_cast must be a non-empty set of strings.
    :postcondition: Returns a dictionary with the counts:
                    - "voters_count": Number of registered voters who voted.
                    - "non_voters_count": Number of unregistered voters who voted.
                    - "unregistered_voters_count": Number of unregistered voters who tried to vote.
    :return: A dictionary with the counts for voters_count, non_voters_count, and unregistered_voters_count.
    :raises TypeError: If the inputs are not sets.

    >>> test_registered_voters = {"voter123", "voter456", "voter789"}
    >>> test_votes_cast = {"voter123", "voter999", "voter789", "voter555"}
    >>> analyze_votes(test_registered_voters, test_votes_cast)
    {'voted_count': 2, 'non_voters_count': 1, 'unregistered_voters_count': 2}

    >>> test_registered_voters = {"voter123", "voter456"}
    >>> test_votes_cast = {"voter999", "voter555"}
    >>> analyze_votes(test_registered_voters, test_votes_cast)
    {'voted_count': 0, 'non_voters_count': 2, 'unregistered_voters_count': 2}

    >>> test_registered_voters = set()
    >>> test_votes_cast = {"voter999"}
    >>> analyze_votes(test_registered_voters, test_votes_cast)
    {'voted_count': 0, 'non_voters_count': 0, 'unregistered_voters_count': 1}
    """