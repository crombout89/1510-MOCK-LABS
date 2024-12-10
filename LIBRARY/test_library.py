import unittest
from library import (
    read_file,
    calculate_average_page_count,
    books_published_after,
    count_books_by_genre,
    highest_rated_book_by_genre,
    authors_with_multiple_books
)


class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        """Set up sample data for testing."""
        # Mock data simulating the content of books.txt
        self.sample_data = [
            {"title": "Book One", "author": "Author A", "genre": "Fiction", "pages": "300", "year": "1945",
             "rating": "4.5"},
            {"title": "Book Two", "author": "Author B", "genre": "Non-Fiction", "pages": "200", "year": "1955",
             "rating": "3.8"},
            {"title": "Book Three", "author": "Author A", "genre": "Fiction", "pages": "150", "year": "1960",
             "rating": "4.8"},
            {"title": "Book Four", "author": "Author C", "genre": "Fiction", "pages": "400", "year": "2000",
             "rating": "4.0"},
            {"title": "Book Five", "author": "Author D", "genre": "Non-Fiction", "pages": "350", "year": "1980",
             "rating": "4.9"}
        ]

    def test_calculate_average_page_count(self):
        """Test the average page count calculation."""
        avg_pages = calculate_average_page_count(self.sample_data)
        self.assertAlmostEqual(avg_pages, 280.0, places=1)  # Expected average: (300 + 200 + 150 + 400 + 350) / 5

    def test_books_published_after(self):
        """Test filtering books published in or after a certain year."""
        books_after_1950 = books_published_after(self.sample_data, 1950)
        self.assertEqual(len(books_after_1950), 4)  # 4 books were published after 1950
        self.assertIn("Book Two", [book['title'] for book in books_after_1950])

    def test_count_books_by_genre(self):
        """Test counting books by genre."""
        genre_counts = count_books_by_genre(self.sample_data)
        self.assertEqual(genre_counts["Fiction"], 3)  # 3 Fiction books
        self.assertEqual(genre_counts["Non-Fiction"], 2)  # 2 Non-Fiction books

    def test_highest_rated_book_by_genre(self):
        """Test finding the highest-rated book in each genre."""
        highest_rated = highest_rated_book_by_genre(self.sample_data)
        self.assertEqual(highest_rated["Fiction"]["title"], "Book Three")  # Highest-rated Fiction book
        self.assertEqual(highest_rated["Non-Fiction"]["title"], "Book Five")  # Highest-rated Non-Fiction book

    def test_authors_with_multiple_books(self):
        """Test finding authors with more than one book."""
        authors = authors_with_multiple_books(self.sample_data)
        self.assertEqual(len(authors), 1)  # Only "Author A" has more than one book
        self.assertIn("Author A", authors)

    def test_read_file(self):
        """Test reading a file and parsing its contents."""
        # Mock file content as a string
        mock_file_content = "title,author,genre,pages,year,rating\n" \
                            "Book One,Author A,Fiction,300,1945,4.5\n" \
                            "Book Two,Author B,Non-Fiction,200,1955,3.8\n"

        # Simulate reading a file by patching open()
        from unittest.mock import mock_open, patch
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            data = read_file("mock_books.txt")

        # Verify the parsed data
        self.assertEqual(len(data), 2)  # 2 books in the mock file
        self.assertEqual(data[0]["title"], "Book One")
        self.assertEqual(data[1]["author"], "Author B")


if __name__ == '__main__':
    unittest.main()