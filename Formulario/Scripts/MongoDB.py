from pymongo import MongoClient 

def MongoConnection():
    
    global collection
    
    try:
        
        MONGO_URI = "mongodb://localhost:27017"

        conn = MongoClient(MONGO_URI)
        db   = conn['Formularies']
        collection = db['User_Information']
        HostName = f"{conn.HOST}:{conn.PORT}"
        
        print( '        ├───────────────────┬─────────────────┬──────────────────┬──────────────────┤')
        print( '        │ STATUS CONNECTION │    HOST NAME    │  DATA BASE NAME  │  DOCUMENT NAME   │')
        print( '        ├───────────────────┼─────────────────┼──────────────────┼──────────────────┤')
        print(f'        │      ONLINE       │ {HostName} │   {db.name}    │ {collection.name} │')
        print( '        ├───────────────────┴─────────────────┴──────────────────┴──────────────────┤')
      
    except:
        
        print( '        ├───────────────────┬─────────────────┬──────────────────┬──────────────────┤')
        print( '        │ STATUS CONNECTION │    HOST NAME    │  DATA BASE NAME  │  DOCUMENT NAME   │')
        print( '        ├───────────────────┼─────────────────┼──────────────────┼──────────────────┤')
        print(f'        │      OFFLINE      │ {HostName} │   {db.name}    │ {collection.name} │')
        print( '        ├───────────────────┴─────────────────┴──────────────────┴──────────────────┤')
     
def MongoInsert(Personal_data):
    
    collection.insert_one(Personal_data)
    
def MongoShow():
    
    result = collection.find()
    
    for i in result:
        
        print(i)