# Project README: Flask-based Bookstore Web Application

## Overview
This Flask application serves as a web interface for a bookstore. It provides functionalities like displaying books, searching for books based on different criteria, and viewing detailed information about each book.

## Key Features
- Display all books on the homepage.
- Search for books by title or other attributes.
- View detailed information about each book including genre, publisher, year published, ISBN, cost, units available, and author information.
- Link to purchase books on Amazon.

## File Structure
- `__pycache__/` - Compiled Python files for faster loading.
- `flask/` - Flask framework files.
- `static/` - Contains static files like CSS, JS, and images.
- `templates/` - Contains HTML templates for different pages.
  - `index.html` - Homepage displaying all books.
  - `found.html` - Page showing search results.
  - `bookpage.html` - Page showing detailed information about a specific book.
  - `about.html` - About page.
- `app.py` - The main Flask application file.
- `Procfile` - Specifies the commands that are executed by the app on startup.
- `README.md` - Markdown file with details about the project.
- `requirements.txt` - A list of Python packages that the app depends on.
- `sorts.py` - Contains sorting algorithms (if applicable).
- `utils.py` - Contains utility functions and MongoDB connection setup.

## Setup and Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`
**Project uses Mongo Database that has to be set up for website to work

## Routes
- `/` - Homepage displaying all books.
- `/found/` or `/found/<bookname>` - Search results page.
- `/about` - About page.
- `/bookpage/<book>` - Detailed book page.
- `/books/<genre>` - Books filtered by genre.

## Database Connection (`utils.py`)
- MongoDB is used for data storage.
- Connects to a MongoDB database named `bookstore` and accesses the `books` collection.
