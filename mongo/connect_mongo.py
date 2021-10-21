import ssl
from pymongo import MongoClient
import urllib.parse
import os
import pandas as pd

def connect_mongo():
    database_nm = "database name"
    collection_nm = "collection name"
    uri = f'mongodb://username:'+urllib.parse.quote_plus('password')+'@hostname:port/{database_nm}'
    certs = r'windows certs path'
    client = MongoClient(uri,
                         ssl=True,
                         ssl_ca_certs=certs,
                         ssl_match_hostname=False)
    db = client.database
    try: 
        collection = db.get_collection(collection_nm)
        ## Print the total number of documents in a collection
        print(collection.count())
        ## Print the ONE sample document
        print(collection.find_one())
        ## Create the mongo query
        mon_query = {"attribute name":"attribute value"}
        mon_data = collection.find(mon_query)
        ## In order to pull all the documents in the collection 
        mon_data = collection.find()
        ## Print each document by looping the above dataset
        for doc in mon_data:
            print(doc)
        #
        ## Integrating with Pandas
        df = pd.DataFrame.from_records(mon_data)
        ## Print the rows count available in dataframe
        print(df.count())
        
    except Exception as e: print(e)
    else: print("Successfully executed !!")
    client.close()

if __name__ == "__main__":
    connect_mongo()