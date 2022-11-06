from app import app
from models.book import *
from models.books import *
from flask import render_template, request, redirect

@app.route('/books')
def index():
    return render_template('index.html', title="List Of Books", books=list_of_books)

@app.route('/books/<index>')
def choose_book(index):
    one_book = list_of_books[int(index)]
    return render_template('single_book.html', title="Chosen Book", book=one_book)

@app.route('/books', methods=['POST'])
def adding_to_main_list():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    available = True if 'checkbox' in request.form else False
    newbook_to_add = Book(title=title, author=author, genre=genre, available=available)
    add_book(newbook_to_add)
    return redirect('/books')

@app.route('/books/delete/<title>', methods=['POST'])
def delete_book(title):
    remove_book(title)
    return redirect('/books')