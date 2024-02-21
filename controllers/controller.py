from flask import render_template, request, redirect
from models.books import books, add_new_book, delete_book
from models.book import Book
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/books')
def books_index():
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

@app.route('/book/<string:title>', methods=['GET'])
def book_details(title):
    book_to_show = None
    for book in books:
        if book.title == title:
            book_to_show = book
            break

    if book_to_show is not None:
        return render_template('book_details.html', book=book_to_show)


@app.route("/books/delete", methods=['POST'])
def delete():
    title = request.form['title']
    delete_book(title)
    return redirect('/books')



