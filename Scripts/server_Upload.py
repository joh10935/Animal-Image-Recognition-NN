##The only thing working on this script is the Public MongoDB connection LMAO


from flask import Flask
from flask_pymongo import PyMongo, MongoClient
import csv
import pymongo
#import dnspython


app = Flask(__name__)


#use flask pymongo to set up the connection to the database
app.config['MONGO_CONNECT'] = False
client = MongoClient("mongodb+srv://FinalProject5Admin:crXD!E&zMpj9Fbs#@cluster0.1f8gahm.mongodb.net/?retryWrites=true&w=majority")
db = client.images

@app.route("/")
def index():
    return "index holder"

@app.route("/freshPull")
def scrape():
    #reference to a database collection (table)
    pictureTable = db.pictureData

    #drop the table if it exists
    db.pictureData.drop()

    #call picture info script
    urlData = csv.reader('../Resources/link.txt')

    print(urlData)

    pictureTable.insert_one(uploadTransform.pullDataButterfly(2112))

    #print(butterflyData)

    return "done?"


if __name__ == "__main__":
    app.run()


# #client = pymongo.MongoClient("mongodb+srv://FinalProject5Admin:crXD!E&zMpj9Fbs#@cluster0.1f8gahm.mongodb.net/?retryWrites=true&w=majority")
# # db = client.test


for image in imageDict:
    imageDict["pixels"+image] = imageDict.pop(image)