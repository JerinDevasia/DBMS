import pymongo
conn = "mongodb://localhost:27017/"
client = pymongo.MongoClient(conn)
database = client['new']
collection = database['sample']
print(database)
for i in collection.find({'course':'MCA'}):
    print(i)
for i in collection.find({'gender':'female','course':'MCA'}):
    print(i['name']['fname']+" "+i['name']['lname'],i['mark'])

for i in collection.find({'course':'MCA'}).sort('mark:-1').limit(1):
    print(i['name']['fname']+" "+i['name']['lname'],i['mark'])

for i in collection.find({'gender':'male','grade':'A+'}):
    print(i['name']['fname']+" "+i['name']['lname'],i['grade'])

for i in collection.find({'course':'Mechanical'}).sort('mark:-1').limit(3):
    print(i['name']['fname']+" "+i['name']['lname'])

for i in collection.find({'gender':'female','mark':{'$gt':90}}):
    print(i['name']['fname']+" "+i['name']['lname'])

for i in collection.find({'mark':{'$gt':80, '$lt':90}}):
    print(i['name']['fname']+" "+i['name']['lname'])

for i in collection.find():
    if(i['name']['fname'].startswith('V')):
        print(i['name']['fname']+" "+i['name']['lname'])

for i in collection.find({'address.city':'Kollam'}):
    print(i)

for i in collection.find({'address.city':{'$nin':('Kollam','Thiruvananthapuram')}}):
    print(i['name']['fname'],i['address']['city'])

for i in collection.find({'gender':'female','address.city':{'$in':('Kollam','Thiruvananthapuram')}}):
    print(i['name']['fname'],i['address']['city'])