# Flask-based Bookstore Web Application

![#009879](https://github.com/gabrielrosendo/sortedTale/assets/71938938/5cc194b8-bfa0-4bc5-a4a7-be5bbd6710d8)

## Overview
This Flask application serves as a web interface for a bookstore. It provides functionalities like displaying books, searching for books based on different criteria, and viewing detailed information about each book.

## Key Features
- Display all books on the homepage.
- Search for books by title or other attributes.
- View detailed information about each book including genre, publisher, year published, ISBN, cost, units available, and author information.
- Link to purchase books on Amazon.


## Setup and Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`
**Project uses Mongo Database that has to be set up for website to work


## Database Connection (`utils.py`)
- MongoDB is used for data storage.
- Connects to a MongoDB database named `bookstore` and accesses the `books` collection.
