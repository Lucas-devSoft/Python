from pymongo import MongoClient

def MongoConnection():
   
   try:

        global collection, db
        
        conn = MongoClient(host="mongodb://localhost",port=27017,connect=True)
        db = conn.get_database('Formularies')
        collection = db.get_collection('User_Information') 
        
   except :
       
       print('error') 
          

def MongoInsert(Personal_data):
        
    collection.insert_one(Personal_data)

def MongoShow():
    
    try:
        
        for i in collection.find():

            print(i)
        
    except:
        
        print('You can not see your information because you are not connected to data base or the information not saved')
    
    