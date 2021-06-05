
# Connect to server
import psycopg2
conn = psycopg2.connect(dbname= 'postgres', host= 'localhost', user= 'postgres', password= 'galvanize')

#Instantiate the curser
cur = conn.cursor()

#Commits
conn.autocommit = True

#Create a database
cur.execute('DROP DATABASE IF EXISTS temp;')
cur.execute('CREATE DATABASE temp;')

cur.close()
conn.close()






SELECT userid, tmstmp as reg_date
INTO TEMPORARY TABLE reg_table
FROM registrations

CREATE TEMPORARY TABLE logins_7d_2014_08_14 AS
SELECT userid, COUNT(*) AS cnt
FROM logins
WHERE logins.tmstmp > timestamp '2014-08-14' - interval '7 days'
GROUP BY userid


SELECT reg.userid, reg.reg_date, login_7d.cnt  as logins_7d, optout.userid opt_out, 
(select max(logins.tmstmp) last_login, from logins group by logins.userid)
FROM reg_table reg
LEFT JOIN logins_7d_2014_08_14 login_7d 
	ON reg.userid=login_7d.userid	
left join optout 
	on reg.userid = optout.userid 
left join logins
	on reg.userid = logins.userid
	
