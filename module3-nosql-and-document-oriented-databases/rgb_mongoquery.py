# module3-nosql-and-document-oriented-databases/rgb_mongoquery.py

import pymongo
import sqlite3

conn = sqlite3.connect('module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()

print(dir(conn))

client = pymongo.MongoClient("MONGO_URL")
db = client.test

characters = 'SELECT * FROM charactercreator_character;'
keys = ('character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom')
df = curs.execute(characters).fetchall()

def get_list_of_dict(keys, list_of_tuples):
    list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
    return list_of_dict

docs = get_list_of_dict(keys, df)
# db.test.remove({})
# db.test.insert_many(docs)

column_names = "PRAGMA table_info(charactercreator_character);"
print(list(curs))
print(list(db.test.find()))