import psycopg2
DB_HOST="localhost"
DB_NAME="library"
DB_USER="postgres"
DB_PASS="admin"
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
cur = conn.cursor()
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('1HG35JE','Harry Potter and the Goblet of Fire','JK Rowling','2000','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('2AA13HE','A Little Life','Hanya Yanagihara','2015','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('3CN22BE','Chronicles: Volume One','Bob Dylan','2004','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('4TL17MT','The Tipping Point','Malcolm Gladwell','2000','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('5DR8NS','Darkmans','Nicola Barker','2007','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('7LN5MT','Light','M John Harrison','2002','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('8BE9LD','Bad Blood','Lorna Sage','2002','Available')")
cur.execute("INSERT INTO books(code,title,author,released,status) VALUES ('9TY18DG','The Cost of Living','Deborah Levy','2018','Available')")

conn.commit()