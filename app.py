import utils
from flask import Flask, render_template, request

app = Flask(__name__)

bookshelf = utils.bookshelf

collection = utils.collection
print(bookshelf)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', books=bookshelf)

@app.route('/found/', defaults={'bookname': ''}, methods=['GET', 'POST'])
@app.route('/found/<path:bookname>', methods=['GET', 'POST'])
def found(bookname):
    if request.method == 'POST' or bookname:
        search_term = str(bookname or request.form.get("bookname")).strip()
        book = collection.find_one({"title": search_term.lower()})
        if book:
            return render_template('found.html', bookname=book)
        else:
            return render_template('found.html', error="Book not found")
    return render_template('found.html', error="Book not found")


if __name__ == '__main__':
    app.run(debug=True)
