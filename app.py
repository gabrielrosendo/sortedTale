import utils
from flask import Flask, render_template, request

app = Flask(__name__)

bookshelf = utils.bookshelf

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tgt = request.form['bookName']
        return render_template('found.html', name=tgt)
    return render_template('index.html', books=bookshelf)

@app.route('/found/<path:name>', methods=['GET', 'POST'])
def found(name):
    located = True
    if request.method == 'POST':
        if name:
            for book in bookshelf:
                if name.lower() == book['title'].lower():
                    return render_template('found.html', book=book)
            located = False
            return render_template('found.html', book=book, error = "Book not found")
    else:
        for book in bookshelf:
            print(book)
            if name.lower() == book['title'].lower():
                return render_template('found.html', book=book)
        return render_template('found.html', book=book, error = "Book not found")


if __name__ == '__main__':
    app.run(debug=True)
