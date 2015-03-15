#!/usr/bin/env python
import mysql.connector
import os
import re


#Obtain WordPress SQL credentials from wp-config.php (DB_NAME,DB_USER,DB_PASSWORD,DB_HOST)






#Open a connection to the database
#The current site url is stored in wp_options(option_name=siteurl, option_value=$siteurl). We'll call this value dev_site_url






#Query for the current site URL (dev_site_url==SELECT option_value FROM wp_options where option_name ="siteurl";)









#In db.sql, replace all instances of the string "localhost" with siteurl EXCEPT in the case of the wp_posts table
#In the wp_posts table, replace all instance of the string "localhost" with siteurl (including in content) except
#for the instances occuring within a guid value (guid is the 18th value inserted into the wp_post table)


#Open sql dumpfile (assume db.sql) stored in root directory (/var/www/html)
with open ('db.sql', 'r+') as sql_dump:
	sql_dump_str = sql_dump.read()
	#find the position of the string "CREATE TABLE wp_posts" and call it wp_posts_start
	wp_posts_start = sql_dump_str.find("INSERT INTO `wp_posts`")
	#find the end of the CREATE TABLE wp_posts statement and call it wp_posts_end_pos
	wp_posts_end = sql_dump_str.find(");", wp_posts_start)
	
	print "wp_posts_start = ",
	print wp_posts_start
	print "wp_posts_end = ",
	print wp_posts_end
	
	print "start: " + sql_dump_str[wp_posts_start:wp_posts_start + 20]
	print "end" + sql_dump_str[wp_posts_end-20:wp_posts_end]
	
	#replace all instances of "localhost" before create wp_posts_start and after wp_posts_end with siteurl
	
	#process the text between wp_posts_start and wp_posts_end_pos
		#Create a replacement string for this part. Call it new_wp_posts
		
		#Save the text between wp_posts_start and wp_posts_end into a list of sub-strings by splitting on newline
		#Call that list rows
		
		#Split each row into elements (on unescaped comma)
		
		#For each row
			#
			
			#string replace "localhost" with 

#Close db. sql




#Drop all tables in the database and then run the db.sql file






#Cut a hole in the box






