import sqlite3

connection = sqlite3.connect("db.sqlite3")


def create_books():
    connection.execute("CREATE TABLE IF NOT EXISTS books(title TEXT, autohor TEXT, publication_date TEXT);")


def create_reviews():
    connection.execute("CREATE TABLE IF NOT EXISTS reviews (name TEXT, location TEXT, reviews_count INTEGER);")


def add_books():
    book = input('Insert your book name: ')
    author = input('Author name: ')
    year = input('Publication year: ')

    connection.execute(
        "INSERT INTO books (title, autohor, publication_date) VALUES (?, ?, ?);",
        (book, author, year)
    )

    connection.commit()
    print('New data has been added')


def show_books():
    data = connection.execute("SELECT * FROM books;")
    for row in data:
        print(row)

create_books()
create_reviews()
add_books()
show_books()