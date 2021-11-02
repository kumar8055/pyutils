from pymongo import MongoClient

def CopyFromColl1ToColl2(database1,collection1,database2,collection2):
    db1 = MongoClient('mongodb://127.0.0.1:27017')[database1][collection1]
    # db2 = MongoClient('mongodb://127.0.0.1:27017')[database2][collection2]
    #here you can put the filters you like.
    for a in db1.find():
        try:
            # db2.insert(a)
            print(a)
        except:
            print('did not copy')

# You can choose the database name and the collection name
CopyFromColl1ToColl2('database1','collection1','database2','collection2')