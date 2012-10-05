from invenio.dbquery import run_sql

for table, in run_sql("SHOW TABLES LIKE 'bib__x'"):
    run_sql('ALTER TABLE %s MODIFY COLUMN `id` int(10) unsigned NOT NULL auto_increment' % table)
    run_sql('ALTER TABLE %s DROP KEY `kv`' % table)
    if table in ('bib85x', 'bib99x', 'bib50x'):
        run_sql('ALTER TABLE %s ADD KEY `kv` (value(250))' % table)
    else:
        run_sql('ALTER TABLE %s ADD KEY `kv` (value(100))' % table)

    print 'Done %s.' % table

for table, in run_sql("SHOW TABLES LIKE 'bibrec_bib__x'"):
    run_sql("ALTER TABLE %s MODIFY COLUMN `id_bibrec` int(10) unsigned NOT NULL default '0'" % table)
    run_sql("ALTER TABLE %s MODIFY COLUMN `id_bibxxx` int(10) unsigned NOT NULL default '0'" % table)

    print 'Done %s.' % table


run_sql('ALTER TABLE bibfmt MODIFY COLUMN `id` int(10) unsigned NOT NULL auto_increment')
run_sql("ALTER TABLE bibfmt MODIFY COLUMN `id_bibrec` int(10) unsigned NOT NULL default '0'")

print 'Done bibfmt.'

run_sql('ALTER TABLE bibrec MODIFY COLUMN `id` int(10) unsigned NOT NULL auto_increment')
# This composite key is useful for MontySolr indexing as there is a need to
# sort by id AND modification date.
run_sql('ALTER TABLE bibrec ADD KEY `id_modif` (modification_date, id)')

print 'Done bibrec.'
