import pymongo

# set up a conninsection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# specify the database and collection you want to insert data into
db = client["mybookstore"]
collection = db["book_information"]

# create a dictionary with the data you want to insert
results = collection.find()
bookshelf =[]
# print results
for book in results:
    bookshelf.append(book)
print(bookshelf)