from models.book import Book

book1 = Book("The Best Book Ever", "Jeff Jefferson", "Horror", False)
book2 = Book("The Mysterious Mystery", "Sam Sammerson", "Thriller", True)
book3 = Book("The Life Of A Goose", "Goose Duck", "Autobiography", False)

list_of_books = [book1, book2, book3]

def add_book(book_name):
    list_of_books.append(book_name)

def remove_book(book_name):
    book_to_remove = None
    for book in list_of_books:
        if book.title == book_name:
            book_to_remove = book
    list_of_books.remove(book_to_remove)
    