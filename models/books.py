from models.book import *

book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780446310789", True)
book2 = Book("1984", "George Orwell", "Dystopian", "9780451524935", False)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Tragedy", "9780743273565", True)
book4 = Book("Pride and Prejudice", "Jane Austen", "Romance", "9780141040349", False)
book5 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", "9780316769174", True)
book6 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", "9780547928227", False)
book7 = Book("Fahrenheit 451", "Ray Bradbury", "Dystopian", "9781451673319", True)
book8 = Book("Moby-Dick", "Herman Melville", "Adventure", "9781503280786", False)
book9 = Book("War and Peace", "Leo Tolstoy", "Historical Fiction", "9781400079988", True)
book10 = Book("The Odyssey", "Homer", "Epic", "9780143039952", False)

books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

def add_new_book(book):
    books.append(book)

def delete_book(title_to_delete):
    book_to_delete = None
    for book in books:
        if book.title == title_to_delete:
            book_to_delete = book 
            break
    if book_to_delete is not None:
        books.remove(book_to_delete) 
    else:    
        print(f"No book found with the title {title_to_delete}")