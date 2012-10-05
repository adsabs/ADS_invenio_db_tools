from invenio.dbquery import run_sql

for table, in run_sql("SHOW TABLES LIKE 'bib__x'"):
    #I delete the old table
    run_sql('DROP TABLE %s' % table)
    #I create the new version that is case sensitive
    if table in ('bib85x', 'bib99x', 'bib50x'):
        kv_value = '250'
    else:
        kv_value = '100'
    
    run_sql("CREATE TABLE `%s` (\
            `id` int(10) unsigned NOT NULL AUTO_INCREMENT,\
            `tag` varchar(6) NOT NULL DEFAULT '',\
            `value` mediumtext NOT NULL,\
            `value_hash` varchar(100) NOT NULL,\
            PRIMARY KEY (`id`),\
            UNIQUE KEY `ktv` (`tag`,`value_hash`),\
            KEY `kt` (`tag`),\
            KEY `kv` (`value`(%s)),\
            KEY `kvh` (`value_hash`)\
            ) ENGINE=MyISAM DEFAULT CHARSET=utf8" % (table, kv_value))
    print 'Done table %s' % table
    
    

#bibcode with problem with text 2004ApJS..151..299H

