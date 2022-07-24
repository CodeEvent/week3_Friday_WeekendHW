from flask import Flask, render_template, request, redirect
from app import banana
from modules.book import Book
from modules.book_list import all_books, add_a_book, delete_book 

@banana.route('/books')
def index():
    return render_template('books.html', title='My list of books', books=all_books)

@banana.route('/books/new')
def new_book():
    return render_template('a_new_book.html', title='New Book')

@banana.route('/books', methods=['POST'])
def create_book():
    print(request.form)
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_a_book(new_book)
    return redirect('/books')

@banana.route('/books/delete/<book>', methods=['POST'])
def delete_book_by_index(book):
    delete_book(int(book))
    return redirect('/books')


    
