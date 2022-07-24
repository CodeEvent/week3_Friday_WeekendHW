from modules.book import Book

book1 = Book('book1_title','book1_author','book1_genre')
book2 = Book('book2_title','book2_author','book2_genre')
book3 = Book('book3_title','book3_author','book3_genre')


all_books = [book1, book2, book3]

def add_a_book(book):
    all_books.append(book)

def delete_book(book):
    all_books.pop(book)
