import unittest
from unittest.mock import mock_open, patch
from grades_analysis import (
    read_file, calculate_subject_averages, find_top_students,
    count_students_in_grade_ranges, highest_grade_per_subject
)


class TestStudentGrades(unittest.TestCase):

    def setUp(self):
        """
        Set up mock data to be used in multiple tests.
        """
        # Mock data as a list of dictionaries
        self.data = [
            {"name": "Alice", "subject": "Math", "grade": "95"},
            {"name": "Bob", "subject": "Math", "grade": "85"},
            {"name": "Charlie", "subject": "Science", "grade": "75"},
            {"name": "Alice", "subject": "Science", "grade": "90"},
        ]

        # Mock file content as a CSV string
        self.mock_file_content = (
            "name,subject,grade\n"
            "Alice,Math,95\n"
            "Bob,Math,85\n"
            "Charlie,Science,75\n"
            "Alice,Science,90\n"
        )

    def test_read_file(self):
        """
        Test the read_file function to ensure it reads and parses data correctly.
        """
        # Patch the built-in open function to simulate file reading
        with patch("builtins.open", mock_open(read_data=self.mock_file_content)):
            data = read_file("mock_grades.txt")  # Filename is irrelevant due to patching

            # Validate the parsed data
            self.assertEqual(len(data), 4)  # Ensure all rows are read
            self.assertEqual(data[0]["name"], "Alice")  # Check first student's name
            self.assertEqual(data[1]["subject"], "Math")  # Check second student's subject
            self.assertEqual(data[2]["grade"], "75")  # Check third student's grade

    def test_calculate_subject_averages(self):
        """
        Test the calculation of average grades for each subject.
        """
        averages = calculate_subject_averages(self.data)
        self.assertEqual(averages["Math"], 90.0)  # Average of 95 and 85
        self.assertEqual(averages["Science"], 82.5)  # Average of 75 and 90

    def test_find_top_students(self):
        """
        Test finding students with grades above a certain threshold.
        """
        top_students = find_top_students(self.data, threshold=90)
        self.assertEqual(len(top_students), 1)  # Only Alice has grades > 90
        self.assertEqual(top_students[0]["name"], "Alice")  # Check the top student

    def test_count_students_in_grade_ranges(self):
        """
        Test counting students in predefined grade ranges.
        """
        grade_ranges = count_students_in_grade_ranges(self.data)
        self.assertEqual(grade_ranges["90-100"], 1)  # 1 student scored 90–100
        self.assertEqual(grade_ranges["80-89"], 1)  # 1 student scored 80–89
        self.assertEqual(grade_ranges["70-79"], 1)  # 1 student scored 70–79
        self.assertEqual(grade_ranges["60-69"], 0)  # No students in this range
        self.assertEqual(grade_ranges["0-59"], 0)  # No students in this range

    def test_highest_grade_per_subject(self):
        """
        Test finding the student with the highest grade in each subject.
        """
        highest_grades = highest_grade_per_subject(self.data)
        self.assertEqual(highest_grades["Math"]["name"], "Alice")  # Alice has highest Math grade
        self.assertEqual(highest_grades["Math"]["grade"], 95)  # Alice's grade is 95
        self.assertEqual(highest_grades["Science"]["name"], "Alice")  # Alice has highest Science grade
        self.assertEqual(highest_grades["Science"]["grade"], 90)  # Alice's grade is 90


if __name__ == '__main__':
    unittest.main()