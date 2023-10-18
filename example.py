import pymongo
conn = "mongodb://localhost:27017/"
client = pymongo.MongoClient(conn)
database = client['exam2']
collection = database['sample2']
print(database)
myDict = [{'_id':1,
          'name':
          {
              'fname':'Abin',
              'lname':'Bob'
          },
          'mark':25,
          'city':'Alappuzha'
          
          },

          {'_id':2,
          'name':
          {
              'fname':'Alan',
              'lname':'DD'
          },
          'mark':30,
          'city':'Trivandrum'
          }]

x = collection.insert_many(myDict)
for i in collection.find({'city':'Trivandrum'}):
    print(i['name']['fname']+" "+i['name']['lname'])

myQuery = {'mark':25}
newvalue = {'$set':{'mark':50}}
x = collection.update_one(myQuery,newvalue)    

for i in collection.find():
    print(i['name']['fname'],i['mark'])


for i in collection.find():
    if i['name']['fname'] == 'Alan':
        myQuery = {'mark':30}
        newQuery = {'$set': {'mark':70}}
        x = collection.update_many(myQuery,newQuery)
        print(i['name']['fname'],i['mark'])
