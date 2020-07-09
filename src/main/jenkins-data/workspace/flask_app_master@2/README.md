# flask_app
run a web application via docker by using flask and psycopg2


In order to run the application there is some configuration to bring. 
Thank you to follow these steps:

I)	Data base configuration 

    To bring the minimum change on the code lets create a PostgreSQL with this configuration:
        Name: postgres
        Password: superUser123
        host: localhost
        port: 5433
      
    Save this and create inside a database name mydb
	
    Finally please run the python code name model_db.py, this code will allow to create table and save inside some data for tests
    If you cannot do these modifications, update files to apply your own values

    Update the file pg_hba.conf
    -	This file is located in the folder C:\Program Files (x86)\pgsql\PostgreSQL\9.5\data this, is the folder chosen at the postgresql    installation.
    -	Update row 80 and 85 by replace 127.0.0.1/32 by 0.0.0.0/0

    This update will allows connection to the database from the container in docker

II)	app.py configuration

    In this section, in file app.py, we have just to update the value host by giving YOUR address ip to be able to make connection from Docker to PostgreSQL
    To get the address ip open cmd, write ipconfig, and take your ip address, it's save under section "Carte réseau sans fil Wi-Fi :" and you take "Adresse IPv4".
 
Now you are ready to run application:
-	open cmd and go to the folder which contain all files (here is named flask_app) and write docker-compose up

when container is runing please open localhost:5000/ to use the app or localhost:5000/mapView to use map location
