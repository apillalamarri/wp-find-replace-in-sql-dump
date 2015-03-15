import mysql.connector
from mysql.connector import errorcode
import os
import re



#Obtain WordPress SQL credentials from wp-config.php (DB_NAME,DB_USER,DB_PASSWORD,DB_HOST)

wp_config = open('~/var/www/html/wp-config.php','r').read()

def get_cred_value(cred_name,wp_config):
    offset=len(cred_name)+4
    cred_name_pos = wp_config.find(cred_name, 0, len(wp_config))
    cred_name_endpos = wp_config.find("');",cred_name_pos)
    cred_name_string=wp_config[cred_name_pos + offset:cred_name_endpos]
    return cred_name_string

db_name = get_cred_value('DB_NAME',wp_config)
db_user = get_cred_value('DB_USER',wp_config)
db_pass = get_cred_value('DB_PASSWORD',wp_config)
db_host = get_cred_value('DB_HOST',wp_config)

#Open a connection to the database
#The current site url is stored in wp_options(option_name=siteurl, option_value=$siteurl). We'll call this value dev_site_url
db = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor=db.cursor()

#Query for the current site URL (dev_site_url==SELECT option_value FROM wp_options where option_name ="siteurl";)
query = ("SELECT option_value FROM wp_options WHERE option_name = 'siteurl'")

#Loop through the cursor object, find the single value, and set that value to siteurl 
cursor.execute(query)
for (item) in cursor:
    siteurl=item
siteurl=item[0]
cursor.close()
db.close()





#Open sql dumpfile (assume db.sql) stored in root directory (/var/www/html)






#String replace all instances of the string "localhost" with dev_site_url EXCEPT in the case of the wp_posts table






#In the wp_posts table, replace all instance of the string "localhost" with dev_site_url (including in content) except for the instances occuring within a guid value (guid is the 18th value inserted into the wp_post table)






#Close db. sql






#Drop all tables in the database and then run the db.sql file






#Cut a hole in the box






