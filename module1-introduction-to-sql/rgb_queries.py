#- How many total Characters are there?
#- How many of each specific subclass?
#- How many total Items?
#- How many of the Items are weapons? How many are not?
#- How many Items does each character have? (Return first 20 rows)
#- How many Weapons does each character have? (Return first 20 rows)
#- On average, how many Items does each Character have?
#- On average, how many Weapons does each character have?


import os
import sqlite3

# read in
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'rpg_db.sqlite3')
conn = sqlite3.connect(DB_FILEPATH)

# instantiate object 
curs = conn.cursor()

# write the query
query = """
SELECT
  c.character_id
  ,c.name as char_name
  ,count(inv.item_id) as item_count
  ,count(w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
GROUP BY c.character_id
LIMIT 20
    """
# execute the query for results. This returns the results object, but not fetched
#curs.execute(query)

# actually display results
result2 = curs.execute(query).fetchall()
print("RESULT", result2)


# How many characters?
# 302
curs.execute('''SELECT count(distinct character_id)
    FROM charactercreator_character;'''

# How many of each specific subclass?
# Mage 108, fighter 68 , theif 51, cleric 75
curs.execute('''SELECT
   c.character_id
   ,c.name as char_name
   ,count(mage.character_ptr_id) as mage_count
   ,count(fighter.character_ptr_id) as fighter_count
   ,count(thief.character_ptr_id) as thief_count
   ,count(cleric.character_ptr_id) as cleric_count
 FROM charactercreator_character c
 LEFT JOIN charactercreator_mage as mage ON mage.character_ptr_id = c.character_id
 LEFT JOIN charactercreator_fighter as fighter ON fighter.character_ptr_id = c.character_id
 LEFT JOIN charactercreator_thief as thief ON thief.character_ptr_id = c.character_id
 LEFT JOIN charactercreator_cleric as cleric ON cleric.character_ptr_id = c.character_id;''')


# How many total items, How many items are not weapons?
# items (174 rows)
# weapons (37)
# non weapon  (137)
curs.execute(''' SELECT 
	sum(w.item_ptr_id is null) as non_weapon_count,
	sum(w.item_ptr_id is not null) as weapon_count
 FROM armory_item i
 LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id;''')

# How many Items does each character have? (Return first 20 rows)
# How many weapons does each character have?
# # start with character, join with weapons, keep joining
# -- How many Weapons does each character have? (Return first 20 rows)
# -- assume: also count 0 for char that don't have weapons
# -- 302 rows (characters)
curs.execute('''SELECT c.character_id
   ,c.name as char_name
   ,count(inv.item_id) as item_count
   ,count(w.item_ptr_id) as weapon_count
 FROM charactercreator_character c
 LEFT JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
 LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
 GROUP BY c.character_id
 LIMIT 20;''')

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
curs.execute('''SELECT
   c.character_id
  ,c.name as char_name
  ,AVG(distinct inv.item_id) as item_count
  ,AVG(w.item_ptr_id) as weapon_count
 FROM charactercreator_character c
 INNER JOIN charactercreator_character_inventory inv ON inv.character_id = c.character_id
 LEFT JOIN armory_weapon w on inv.item_id = w.item_ptr_id
 GROUP BY c.character_id;''')




 