import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Fetch all books
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

# Print the data
for book in books:
    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Rented: {'Yes' if book[3] else 'No'},Quantity:{book[4]}")

# Close the connection
conn.close()
