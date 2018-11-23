import psycopg2

hostname = '0.0.0.0'
username = 'cycloneuser' # the username when you create the database
password = 'abc' #change to your password
database = 'cyclonedata'


def queryQuotes( conn ) :
    cur = conn.cursor()
    cur.execute( """CREATE TABLE public.cyclone
(
    storm_identifier text NOT NULL,
    track_history text,
    forecast_history text
);""")
    cur.execute( """select * from cyclone""" )
    rows = cur.fetchall()

    for row in rows:
        print(row[0])


conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
conn.autocommit = True
queryQuotes(conn)
conn.close()