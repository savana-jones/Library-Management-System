import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the database with rental status and queue information
def init_db():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_rented INTEGER DEFAULT 0
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS waiting_queue (
                book_id INTEGER,
                user_email TEXT,
                PRIMARY KEY (book_id, user_email)
            )
        """)
        conn.commit()

init_db()

# Route to display all books
@app.route('/')
def index():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
    return render_template('index.html', books=books)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        # Search for books with titles or authors matching the keyword
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        search_results = cursor.fetchall()
    return render_template('index.html', books=search_results)

# Route to render a form to add a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        
        # Add the new book to the database
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, is_rented) VALUES (?, ?, 0)", (title, author))
            conn.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_book.html')


# Route to rent a book
@app.route('/rent/<int:book_id>')
def rent(book_id):
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
    if not book or book[3]:  # Check if the book is already rented
        return "This book is already rented or does not exist.", 404
    return render_template('rent.html', book=book)
@app.route('/confirm_rent/<int:book_id>', methods=['POST'])
def confirm_rent(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Check if the book is available for rent
    cursor.execute("SELECT quantity FROM books WHERE id = ?", (book_id,))
    quantity = cursor.fetchone()[0]
    
    if quantity > 0:
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book_id,))
        conn.commit()
    
    conn.close()
    return redirect(url_for('index'))


# Route to wait in line for a book
@app.route('/wait_in_line/<int:book_id>', methods=['GET', 'POST'])
def wait_in_line(book_id):
    return render_template('wait_in_line.html', book_id=book_id)

@app.route('/wait_in_new/<int:book_id>', methods=['GET', 'POST'])
def wait_in_new(book_id):
    if request.method == 'POST':
        user_email = request.form['user_email']
        
        # Insert the user's email into the waiting queue
        with sqlite3.connect("library.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO waiting_queue (book_id, user_email) VALUES (?, ?)", (book_id, user_email))
            conn.commit()

        # Redirect to the homepage with a different message key
        return redirect(url_for('index', added_to_waitlist="true"))
    
    return render_template('wait_in_line.html', book_id=book_id)


# Route to return a book
@app.route('/return_book/<int:book_id>', methods=['GET', 'POST'])
def return_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Increase the quantity if it's less than 5
    cursor.execute("UPDATE books SET quantity = MIN(quantity + 1, 5) WHERE id = ?", (book_id,))
    conn.commit()
    
    conn.close()
    return redirect(url_for('index'))

# Notification function (Observer pattern)
def notify_user(email, book_id):
    print(f"Notification sent to {email}: Book with ID {book_id} is now available for rent.")

if __name__ == "__main__":
    app.run(debug=True)
