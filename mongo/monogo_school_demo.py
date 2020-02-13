from pprint import pprint

from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.get_database("my_school")
students = db.get_collection('students')

students.insert_one({
    'name': 'Shira',
    'age': 22,
    'address': {
        'city': 'Jerusalem',
        'street': 'King George'
    }
})

for d in students.find():
    pprint(d)
    print()

xx = students.find({})
print(type(xx))