from typing import Set, Dict

def analyze_votes(registered_voters: Set[str], votes_cast: Set[str]) -> Dict[str, int]:
    """
    Analyze voting results by determining how many registered voters actually voted, how many registered voters did
    not vote, and how many unregistered voters tried to vote.

    :param registered_voters: A set of registered voter IDs (strings).
    :param votes_cast: A set of IDs (strings) of people who cast votes.
    :precondition: registered_voters must be a set of strings.
    :precondition: votes_cast must be a set of strings.
    :postcondition: Returns a dictionary with the counts:
                    - "voted_count": Number of registered voters who voted.
                    - "non_voters_count": Number of registered voters who did not vote.
                    - "unregistered_voters_count": Number of unregistered voters who tried to vote.
    :return: A dictionary with the counts for voted_count, non_voters_count, and unregistered_voters_count.
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

    # Step 1: Validate the inputs
    if not isinstance(registered_voters, set) or not isinstance(votes_cast, set):
        raise TypeError("The inputs must be sets.")

    # Step 2: Find registered voters who voted
    # Use the intersection (&) of registered_voters and votes_cast to find the values in common between both.
    voted_count = len(registered_voters & votes_cast)

    # Step 3: Find registered voters who DID NOT vote
    # Use the difference (-) of registered_voters and votes_cast to find elements in one set that is not in the other.
    non_voters_count = len(registered_voters - votes_cast)

    # Step 4: Find the unregistered voters who tried to vote
    # Use the difference (-) of votes_cast and registered_voters to find values that only exist in votes_cast
    # These values represent the voter IDs that don't match the registered voters set
    unregistered_voters_count = len(votes_cast - registered_voters)

    # Step 5: Return the results as a dictionary
    return {
        "voted_count": voted_count,
        "non_voters_count": non_voters_count,
        "unregistered_voters_count": unregistered_voters_count
    }


def main():
    """Drive the program."""
    # Example inputs
    registered_voters = {"voter1", "voter2", "voter3", "voter4"}
    votes_cast = {"voter1", "voter5", "voter2", "voter6"}

    # Analyze the votes
    results = analyze_votes(registered_voters, votes_cast)

    # Print the results
    print("Voting Analysis Results:")
    print(f"Registered voters who voted: {results['voted_count']}")
    print(f"Registered voters who did not vote: {results['non_voters_count']}")
    print(f"Unregistered voters who tried to vote: {results['unregistered_voters_count']}")


if __name__ == "__main__":
    main()