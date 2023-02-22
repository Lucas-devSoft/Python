from pymongo import MongoClient

def MongoConnection():
    
    global collection
    
    try:
        
        MONGO_URI = "mongodb://localhost:27017"

        connection = MongoClient(MONGO_URI)
        
        database = connection["Calculator"]
        collection = database["History"]
        
    except:
        
      print('An exception occurred conections')

def MongoInsertDB(cont,name,Num1,Operator,Num2,Result):
    
    
    try:
        
      collection.insert_one({"_id"          : cont,
                              "Name_User"   : name,
                              "Value_1"     : Num1,
                              "Operator"    : Operator,
                              "Value_2"     : Num2,
                              "Result"      : Result})
      
    except:
        
      print('│    The data not insert because is not connected to data base of Mongo     │')
    
    
    
    



