

import os
import sqlite3
DB_FILEPATH ='rpg_db.sqlite3'
#DB_FILEPATH = os.path.join(os.path.dirname(_file_), "..", 'chinook.db')

conn = sqlite3.connect('rpg_db.sqlite3')
print("connection", conn)
curs = conn.cursor()
print("cursor", curs)
query = 'SELECT COUNT(*) FROM armory_item;'

result1= curs.execute(query)
print('',result1)
result2= curs.execute(query).fetchall()
print('result2',result2)

query = 'SELECT 
  c.character_id
  ,c.name as char_name
  , count(inv.item_id) as items_count
  ,count (w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory  inv on inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
GROUP BY c.character_id -- row per what?
ORDER BY weapon_count DESC
LIMIT 20;'











