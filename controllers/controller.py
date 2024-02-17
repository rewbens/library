from flask import render_template, request, redirect
from models.books import books, add_new_book, delete_book
from models.book import *
from app import app

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route("/books", methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    isbn = request.form['isbn']
    checkedout = True if request.form['checkedout'].lower() == 'true' else False
    newbook = Book(title=title, author=author, genre=genre, isbn=isbn, checkedout=checkedout)
    add_new_book(newbook)
    return redirect('/books')

@app.route("/books/delete", methods=['POST'])
def delete():
    title = request.form['title']
    delete_book(title)
    return redirect('/books')



