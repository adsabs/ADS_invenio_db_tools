from invenio.dbquery import run_sql

run_sql('delete from collection')
print "removed all the old collections"

run_sql("INSERT INTO collection (id, name, dbquery) VALUES (1, 'ADS metadata repository', NULL)")
run_sql("INSERT INTO collection (id, name, dbquery) VALUES (2, 'Databases', NULL)")
run_sql("INSERT INTO collection (id, name, dbquery) VALUES (3, 'Astronomy', '980__a:ASTRONOMY')")
run_sql("INSERT INTO collection (id, name, dbquery) VALUES (4, 'Physics', '980__a:PHYSICS')")
run_sql("INSERT INTO collection (id, name, dbquery) VALUES (5, 'General', '980__a:GENERAL')")
run_sql("INSERT INTO collection (id, name, dbquery) VALUES (6, 'Preprints', '980__p:EPRINT')")

print "new collection added"

run_sql('delete from collection_collection')
print "removed all the old collections hierarchy"

run_sql("INSERT INTO collection_collection (id_dad, id_son, type, score) VALUES (1, 2, 'r', 1)")
run_sql("INSERT INTO collection_collection (id_dad, id_son, type, score) VALUES (2, 3, 'r', 4)")
run_sql("INSERT INTO collection_collection (id_dad, id_son, type, score) VALUES (2, 4, 'r', 3)")
run_sql("INSERT INTO collection_collection (id_dad, id_son, type, score) VALUES (2, 5, 'r', 2)")
run_sql("INSERT INTO collection_collection (id_dad, id_son, type, score) VALUES (2, 6, 'r', 1)")

print "new collection hierarchy added"
