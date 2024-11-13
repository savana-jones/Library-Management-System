import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database setup function
def init_db():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)
        conn.commit()

# Call this function once to initialize the database
init_db()

# Route to display all books in the library
@app.route('/')
def index():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
    return render_template('index.html', books=books)

# Route to add a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
            conn.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html')

# Route to search for books by keyword
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
        results = cursor.fetchall()
    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
