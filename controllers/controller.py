from app import app
from models.book import *
from models.books import *
from flask import render_template

@app.route('/books')
def index():
    return render_template('index.html', title="List Of Books", books=list_of_books)

@app.route('/books/<index>')
def choose_book(index):
    one_book = list_of_books[int(index)]
    return render_template('single_book.html', title="Chosen Book", book=one_book)