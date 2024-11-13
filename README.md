# Library Management System

This is a simple library management system built using Flask and SQLite. It allows users to view available books, rent books, join a waitlist when books are unavailable, and return books. It also notifies users when a book becomes available.

## Features

- **View Books**: See a list of all available books in the library.
- **Search**: Search for books by title or author.
- **Add a Book**: Add new books to the library (admin feature).
- **Rent a Book**: Rent a book if available; otherwise, join a waitlist.
- **Wait in Line**: If a book is currently rented, users can join the waitlist.
- **Return a Book**: Return a rented book and notify users on the waitlist.
- **Notifications**: Send notifications to users when a book on the waitlist becomes available.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Install required packages**:
   ```bash
   pip install flask
   ```

3. **Initialize the database**:
   Run the app once to initialize the database, which will create `library.db` with the required tables:
   ```bash
   python app.py
   ```

### Database Structure

The project uses SQLite with the following tables:
- `books`: Stores book details including title, author, quantity, and rental status.
- `waiting_queue`: Stores information about users waiting for specific books.

### Running the Application

Run the following command to start the application in development mode:

```bash
python app.py
```

By default, the app runs on `http://127.0.0.1:5000`. Open this URL in your browser to access the Library Management System.

## Routes

- `/` - Home page, displaying all books.
- `/search` - POST route to search for books by title or author.
- `/add_book` - GET and POST routes to add a new book.
- `/rent/<int:book_id>` - GET route to rent a specific book if available.
- `/confirm_rent/<int:book_id>` - POST route to confirm the rental.
- `/wait_in_line/<int:book_id>` - GET and POST routes to join the waitlist for a book.
- `/return_book/<int:book_id>` - POST route to return a book.

## Code Structure

- `app.py`: Main application file with routes and business logic.
- `templates/`: Contains HTML templates for each page.
- `static/`: Contains CSS and other static files.
- `library.db`: SQLite database file generated automatically.

## Usage

1. **Search for a book** by title or author.
2. **Rent a book** if available; otherwise, you can join the waitlist.
3. **Return a book** once you’re done, allowing the next person on the waitlist to rent it.
4. **Admin options** include adding new books to the library.

## Future Improvements

- Add user authentication for admin and users.
- Add email notifications for waitlist updates.
- Track rental history and set return due dates.
