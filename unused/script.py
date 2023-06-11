import utils
import sorts

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']
def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]
def by_total_length(book_a, book_b):
  total_a = len(book_a["title"])+ len(book_a["author"])
  total_b = len(book_b["title"])+ len(book_b["author"])
  return total_a > total_b

bookshelf = utils.bookshelf
bookshelf_v1 = bookshelf.copy()

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
# update each document in the collection with the sorted data
for i, book in enumerate(sort_1):
    query = {"_id": book["_id"]}
    update = {"$set": {"order": i}}
    utils.collection.update_one(query, update)



bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
sorts.quicksort(bookshelf, 0, len(bookshelf)-1, by_total_length)
for i in range(len(bookshelf)):
  print(bookshelf[i]['author_lower'])



