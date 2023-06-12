import utils
from flask import Flask, render_template, request

app = Flask(__name__)

library = utils.bookshelf

collection = utils.collection


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', books=library)

@app.route('/found/', defaults={'bookshelf': ''}, methods=['GET', 'POST'])
@app.route('/found/<path:bookshelf>', methods=['GET', 'POST'])
def found(bookshelf):
    if request.method == 'POST' or bookshelf:
        search_term = str(bookshelf or request.form.get("searchterm")).strip()
        search_option = request.form.get("searchby")
        book_s = collection.find({search_option: search_term})
        if bookshelf:
            return render_template('found.html', bookshelf=book_s)
        else:
            return render_template('found.html', error="Book not found")
    return render_template('found.html', error="Book not found")

@app.route('/about', methods = ['GET', 'POST'])
def about():
  return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
