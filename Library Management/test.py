import psycopg2
DB_HOST="localhost"
DB_NAME="libraryagent"
DB_USER="yassine"
DB_PASS="adpost2008"
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
cur = conn.cursor()
cur.execute("CREATE TABLE reserve (id varchar(45) NOT NULL PRIMARY KEY, bookcode varchar(45));")
conn.commit()