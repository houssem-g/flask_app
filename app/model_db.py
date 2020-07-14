import psycopg2


#instance flask
# app = Flask(__name__)

# login and pwd to access to pg sql (think to use environement variable, more secure)
conn = psycopg2.connect(user="postgres",
                            password="superUser123",
                            host='localhost',
                            port="5433",
                            database="mydb")
cur = conn.cursor()
cur.execute("create table if not exists peaks_locations (id SERIAL PRIMARY KEY, lat float, lon float, altitude float, name varchar(45))")
conn.commit()
cur.execute("INSERT INTO peaks_locations (lat, lon, altitude, name)  VALUES (40.6892, -74.0445, 100, 'Statue de la Liberté'), (48.8584, 2.2945, 324, 'Tour Eiffel'), (48.8738, 2.295, 50, 'Arc de Triomphe');")
conn.commit()
