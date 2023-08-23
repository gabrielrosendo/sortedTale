import pymongo
import certifi
ca = certifi.where()

# set up a conninsection to MongoDB
client = pymongo.MongoClient("mongodb+srv://gabrielrosendo72:CvjdoUSPq49HOxsm@cluster0.tg1qb5x.mongodb.net/", tlsCAFile=ca)

# specify the database and collection you want to insert data into
db = client["bookstore"]
collection = db["books"]

# create a dictionary with the data you want to insert
results = collection.find()
bookshelf =[]
for book in results:
   bookshelf.append(book)