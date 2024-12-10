def read_file(file_name):
    """
    Reads a file and returns its contents as a list of dictionaries.

    Each line of the file represents a record (e.g., a student and their grades),
    and the first line is assumed to contain headers. The function reads the file,
    splits the data into columns based on the headers, and stores each record as
    a dictionary.

    Args:
        file_name (str): The name of the file to read (e.g., 'grades.txt').

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents
                    a record in the file. If the file is not found, returns an
                    empty list.
    """
    data = []
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the first line as column headers
            headers = file.readline().strip().split(',')

            # Read each subsequent line, split values, and create a dictionary
            for line in file:
                values = line.strip().split(',')
                data.append(dict(zip(headers, values)))
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: File '{file_name}' not found.")
    return data


def calculate_subject_averages(data):
    """
    Calculates the average grade for each subject in the data.

    Args:
        data (list[dict]): A list of dictionaries where each dictionary contains
                           information about a student's grade in a subject.

    Returns:
        dict: A dictionary where the keys are subject names, and the values
              are the average grades for those subjects.
    """
    subjects = {}
    for entry in data:
        # Extract the subject and grade from each record
        subject = entry['subject']
        grade = int(entry['grade'])  # Convert grade to integer

        # Initialize the subject in the dictionary if not already present
        if subject not in subjects:
            subjects[subject] = []
        # Add the grade to the subject's list of grades
        subjects[subject].append(grade)

    # Compute the average for each subject
    return {subject: sum(grades) / len(grades) for subject, grades in subjects.items()}


def find_top_students(data, threshold=90):
    """
    Finds students who scored above a given threshold in any subject.

    Args:
        data (list[dict]): A list of dictionaries where each dictionary contains
                           information about a student's grade in a subject.
        threshold (int): The grade threshold to filter students (default is 90).

    Returns:
        list[dict]: A list of dictionaries representing students who scored
                    above the threshold.
    """
    # Filter and return only the records where the grade exceeds the threshold
    return [entry for entry in data if int(entry['grade']) > threshold]


def count_students_in_grade_ranges(data):
    """
    Counts the number of students in predefined grade ranges.

    The grade ranges are:
        - 90–100
        - 80–89
        - 70–79
        - 60–69
        - 0–59

    Args:
        data (list[dict]): A list of dictionaries where each dictionary contains
                           information about a student's grade in a subject.

    Returns:
        dict: A dictionary where the keys are grade ranges (e.g., "90-100"),
              and the values are the number of students in each range.
    """
    # Initialize the grade range counters
    ranges = {
        "90-100": 0,
        "80-89": 0,
        "70-79": 0,
        "60-69": 0,
        "0-59": 0
    }

    for entry in data:
        # Convert the grade to an integer
        grade = int(entry['grade'])

        # Increment the appropriate grade range counter
        if 90 <= grade <= 100:
            ranges["90-100"] += 1
        elif 80 <= grade <= 89:
            ranges["80-89"] += 1
        elif 70 <= grade <= 79:
            ranges["70-79"] += 1
        elif 60 <= grade <= 69:
            ranges["60-69"] += 1
        else:
            ranges["0-59"] += 1

    return ranges


def highest_grade_per_subject(data):
    """
    Finds the student with the highest grade in each subject.

    Args:
        data (list[dict]): A list of dictionaries where each dictionary contains
                           information about a student's grade in a subject.

    Returns:
        dict: A dictionary where the keys are subject names, and the values
              are dictionaries containing the student's name and their grade.
    """
    highest_grades = {}
    for entry in data:
        # Extract the subject, name, and grade
        subject = entry['subject']
        grade = int(entry['grade'])
        name = entry['name']

        # Update the highest grade for the subject if necessary
        if subject not in highest_grades or grade > highest_grades[subject]['grade']:
            highest_grades[subject] = {'name': name, 'grade': grade}

    return highest_grades


def main():
    """
    Main function to orchestrate the program.

    This function reads data from a file, processes the data using various
    functions, and prints the results in a readable format.
    """
    file_name = 'grades.txt'  # Name of the file to read
    data = read_file(file_name)  # Read the file into a list of dictionaries

    # Exit if no data was read (e.g., if the file was not found)
    if not data:
        return

    # Part 1: Calculate and print the average grades by subject
    averages = calculate_subject_averages(data)
    print("Average grades by subject:", averages)

    # Part 2: Find and print students scoring above a threshold
    top_students = find_top_students(data)
    print("Students scoring above 90:", [entry['name'] for entry in top_students])

    # Part 3: Count and print the number of students in each grade range
    grade_ranges = count_students_in_grade_ranges(data)
    print("Number of students in each grade range:", grade_ranges)

    # Part 4: Find and print the highest grade per subject
    highest_grades = highest_grade_per_subject(data)
    print("Highest grade per subject:", highest_grades)


# Entry point for the program
if __name__ == '__main__':
    main()