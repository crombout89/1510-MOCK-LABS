def read_file(file_name):
    """Reads the file and returns the data as a list of dictionaries."""
    data = []
    try:
        with open(file_name, 'r') as file:
            # Read the header row and split it into column names
            headers = file.readline().strip().split(',')
            # Process the remaining lines
            for line in file:
                values = line.strip().split(',')
                # Map headers to values and store as a dictionary
                data.append(dict(zip(headers, values)))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return data


def calculate_average_page_count(data):
    """Calculates and returns the average number of pages."""
    page_counts = [int(book['pages']) for book in data if book['pages'].isdigit()]
    return sum(page_counts) / len(page_counts) if page_counts else 0


def books_published_after(data, year):
    """Returns a list of books published in or after the given year."""
    return [book for book in data if int(book['year']) >= year]


def count_books_by_genre(data):
    """Counts the number of books in each genre."""
    genre_counts = {}
    for book in data:
        genre = book.get('genre', 'Unknown')
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def highest_rated_book_by_genre(data):
    """Finds the highest-rated book in each genre."""
    highest_rated = {}
    for book in data:
        genre = book.get('genre', 'Unknown')
        rating = float(book.get('rating', 0))
        if genre not in highest_rated or rating > highest_rated[genre]['rating']:
            highest_rated[genre] = {'title': book['title'], 'rating': rating}
    return highest_rated


def authors_with_multiple_books(data):
    """Finds authors with more than one book, sorted alphabetically by surname."""
    author_counts = {}
    for book in data:
        author = book.get('author')
        if author:
            author_counts[author] = author_counts.get(author, 0) + 1
    multiple_books = [author for author, count in author_counts.items() if count > 1]
    return sorted(multiple_books, key=lambda name: name.split()[-1])  # Sort by surname


def main():
    file_name = 'books.txt'
    data = read_file(file_name)

    if not data:
        return  # Exit if the file couldn't be read

    # (b) Calculate the average number of pages
    avg_pages = calculate_average_page_count(data)
    print(f"Average number of pages: {avg_pages:.2f}")

    # (c) List books published in or after 1950
    books_after_1950 = books_published_after(data, 1950)
    print("\nBooks published in or after 1950:")
    for i, book in enumerate(books_after_1950, start=1):
        print(f"{i}. {book['title']} ({book['year']})")

    # (d) Count the number of books in each genre
    genre_counts = count_books_by_genre(data)
    print("\nNumber of books by genre:")
    for genre, count in genre_counts.items():
        print(f"{genre}: {count}")

    # (e) Find the highest-rated book in each genre
    highest_rated = highest_rated_book_by_genre(data)
    print("\nHighest-rated book by genre:")
    for genre, book in highest_rated.items():
        print(f"{genre}: {book['title']} (Rating: {book['rating']})")

    # (f) List authors with more than one book
    authors = authors_with_multiple_books(data)
    print("\nAuthors with more than one book:")
    for author in authors:
        print(author)


if __name__ == '__main__':
    main()