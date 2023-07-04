import utils
import re
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

bookshelf = utils.bookshelf

collection = utils.collection


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', books=bookshelf)

@app.route('/found/', defaults={'bookname': ''}, methods=['GET', 'POST'])
@app.route('/found/<path:bookname>', methods=['GET', 'POST'])
def found(bookname):
    if request.method == 'POST' or bookname:
        search_term = str(bookname or request.form.get("bookname")).strip()
        search_option = request.form.get("searchby", "title") 
        bookshelf_results = collection.find({search_option: search_term})
        # Create a regular expression pattern to match the search term as a substring
        regex_pattern = re.compile('.*{}.*'.format(re.escape(search_term)), re.IGNORECASE)
        # Use the regular expression pattern in the MongoDB query
        bookshelf_results = collection.find({search_option: regex_pattern})

        if bookshelf_results:
            return render_template('found.html', bookshelf=bookshelf_results)
        else:
            return render_template('found.html', error="Book not found")
    return render_template('found.html', error="Book not found")
  
@app.route('/about', methods = ['GET', 'POST'])
def about():
  return render_template('about.html')

@app.route('/bookpage/<path:book>', methods=['GET', 'POST'])
def bookpage(book):
    book_details = collection.find_one({"title": book})
    return render_template('bookpage.html', book=book_details)


@app.route('/books/<path:genre>', methods=['GET', 'POST'])
def books_by_genre(genre):
    bookshelf_results = collection.find({"genre": genre})

    if bookshelf_results:
        return render_template('found.html', bookshelf=bookshelf_results)
    else:
        return render_template('found.html', error="No books found in this genre")


if __name__ == '__main__':
    app.run(debug=True)
