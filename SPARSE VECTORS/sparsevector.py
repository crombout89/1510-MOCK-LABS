def sparse_add(vector_a, vector_b):
    """
    Add two sparse vectors together.

    :param vector_a: A dictionary representing a sparse vector. Must contain a "length" key.
    :param vector_b: A dictionary representing a sparse vector. Must contain a "length" key.
    :precondition: vector_a and vector_b must have the same "length" value.
    :precondition: Both input dictionaries must represent valid sparse vectors.
    :postcondition: Returns a dictionary representing the sum of the two vectors in sparse format.
    :return: A dictionary representing the element-wise sum of vector_a and vector_b.

    Example:
    >>> test_vector_a = {"length": 3, 0: 1, 2: 3}
    >>> test_vector_b = {"length": 3, 0: 4, 1: 5, 2: 6}
    >>> sparse_add(test_vector_a, test_vector_b)
    {'length': 3, 0: 5, 1: 5, 2: 9}

    >>> test_vector_a = {"length": 3, 0: 1}
    >>> test_vector_b = {"length": 3, 1: 2}
    >>> sparse_add(test_vector_a, test_vector_b)
    {'length': 3, 0: 1, 1: 2}
    """
    # Step 1: Check that both vectors have the same "length" key.
    if "length" not in vector_a or "length" not in vector_b:
        raise ValueError("Both vectors must have the same 'length' key.")

    # Step 2: Ensure that both 'length' values match
    if vector_a["length"] != vector_b["length"]:
        raise ValueError("Both vectors must have the same length.")

    # Step 3: Find all unique indices across both vectors.
    # Use the union operator (|) to combine the keys from both dictionaries, excluding 'length' key.
    # The union operator also represents the logical OR for sets
    all_indices = (set(vector_a.keys()) | set(vector_b.keys())) - {"length"}

    # Step 4: Initialize the result dictionary and set its 'length' key.
    result = {"length": vector_a["length"]}

    # Step 5: Iterate over all unique indices to compute the sum
    for index in all_indices:
        # Get the value from vector_a at this index, defaulting to 0 if the index is missing.
        value_a = vector_a.get(index, 0)
        # Also get the value from vector_a at this index, defaulting to 0 if the index is missing.
        value_b = vector_b.get(index, 0)

        # Calculate the ELEMENT-WISE sum for this index
        sum_value = value_a + value_b

        # Only store the sum value in the dictionary if the sum is NON-ZERO
        if sum_value != 0:
            result[index] = sum_value

    # Step 6: Return the resulting sparse vector
    return result


def sparse_dot_product(vector_a, vector_b):
    """
    Compute the dot product of two sparse vectors.

    :param vector_a: A dictionary representing a sparse vector. Must contain a "length" key.
    :param vector_b: A dictionary representing a sparse vector. Must contain a "length" key.
    :precondition: vector_a and vector_b must have the same "length" value.
    :precondition: Both input dictionaries must represent valid sparse vectors.
    :postcondition: Returns the dot product as a single number.
    :return: A single number representing the dot product of the two vectors.

    Example:
    >>> test_vector_a = {"length": 3, 0: 1, 2: 3}
    >>> test_vector_b = {"length": 3, 0: 4, 1: 5, 2: 6}
    >>> sparse_dot_product(test_vector_a, test_vector_b)
    22

    >>> test_vector_a = {"length": 3, 0: 1}
    >>> test_vector_b = {"length": 3, 1: 2}
    >>> sparse_dot_product(test_vector_a, test_vector_b)
    0
    """

    # Step 1: Validate the input
    if "length" not in vector_a or "length" not in vector_b:
        raise ValueError("Both vectors must have a 'length' key.")

    if vector_a["length"] != vector_b["length"]:
        raise ValueError("Both vectors must have the same length.")

    # Step 2: Find the common indices
    # Use the intersection operator (&) to find the common indices from both dictionaries, excluding 'length' key.
    # The intersection operator also represents the logical AND for sets
    common_indices = (set(vector_a.keys()) & set(vector_b.keys())) - {"length"}

    # Step 3: Compute the product of the indices
    dot_product = 0
    for index in common_indices:
        dot_product += vector_a[index] * vector_b[index]

    # Step 4: Return the result
    return dot_product



def main():
    """ Drive the program. """


if __name__ == "__main__":
    main()
