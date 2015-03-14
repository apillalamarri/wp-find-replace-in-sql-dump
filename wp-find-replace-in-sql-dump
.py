#!/usr/bin/env python
import mysql.connector
import os
import re


#Obtain WordPress SQL credentials from wp-config.php (DB_NAME,DB_USER,DB_PASSWORD,DB_HOST)






#Open a connection to the database
#The current site url is stored in wp_options(option_name=siteurl, option_value=$siteurl). We'll call this value dev_site_url






#Query for the current site URL (dev_site_url==SELECT option_value FROM wp_options where option_name ="siteurl";)






#Open sql dumpfile (assume db.sql) stored in root directory (/var/www/html)






#String replace all instances of the string "localhost" with dev_site_url EXCEPT in the case of the wp_posts table






#In the wp_posts table, replace all instance of the string "localhost" with dev_site_url (including in content) except for the instances occuring within a guid value (guid is the 18th value inserted into the wp_post table)






#Close db. sql






#Drop all tables in the database and then run the db.sql file






#Cut a hole in the box






