from flask import Flask, jsonify, make_response, request, render_template
from flask_cors import CORS
# import psycopg2
import json

#instance flask
app = Flask(__name__)
CORS(app)
# conn = psycopg2.connect(user="postgres",
#                             password="superUser123",
#                             host='192.168.0.21',
#                             port="5433",
#                             database="mydb")
# cursor = conn.cursor()
@app.route('/')
def main():
   """Render an HTML template and return"""
   return render_template('index.html')
   #variab = "hello houssem"
   #return variab
@app.route('/mapView')
def mapView():
   """Render an HTML template and return"""
   return render_template('viewMap.html')


@app.route('/help')
def func_documentation():
    documentation = open('api_doc.txt', 'r')
    content = documentation.read()
    documentation.close()
    return render_template("api_doc.html")
    

@app.route('/readAllTable', methods=['get', 'post', 'put', 'delete'])
def get_all_data(): 
    
    if request.method == 'GET': 
        print('the adress ip of the user:', request.remote_addr)
        if request.args and len(request.args)> 0:

            postgreSQL_select_Query = "select * from peaks_locations where lat > %s and lon > %s and lat < %s and lon < %s"
            cursor.execute(postgreSQL_select_Query, (request.args['minLat'], request.args['minLon'], request.args['maxLat'], request.args['maxLon']))
            data = cursor.fetchall()
            dictionary = []
            for liste in data:
                newValues = {"latitude" : liste[0], "longitude" : liste[1], "altitude" : liste[2], "name" : liste[3]}
                dictionary.append(newValues)
            print('dictionary:', dictionary)
            response = app.response_class(
                response=json.dumps(dictionary),
                status=200,
                content_type='application/json'
            ) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

        else:
            postgreSQL_select_Query = "select * from peaks_locations"
            cursor.execute(postgreSQL_select_Query)
            data = cursor.fetchall()
            dictionary = []
            for liste in data:
                newValues = {"id": liste[0], "latitude" : liste[1], "longitude" : liste[2], "altitude" : liste[3], "name" : liste[4]}
                dictionary.append(newValues)
            print('dictionary:', dictionary)
            response = app.response_class(
                response=json.dumps(dictionary),
                status=200,
                content_type='application/json'
            ) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            
    if request.method == 'POST':
        dataPost = request.json
        if len(dataPost.values()) != 4 :
            return "please fill all fields"
        latitude = request.json['lat']
        longitude = request.json['lon']
        altitude = request.json['altitude']
        nom = request.json['name']
        print('nom:', nom)
        postgreSQL_select_Query = "INSERT INTO peaks_locations (lat, lon, altitude, name) VALUES (%s, %s, %s, %s);"
        cursor.execute(postgreSQL_select_Query, (latitude, longitude, altitude, nom))
        conn.commit()
        response = jsonify(success=True)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        print('the output to the browser:', response, response.headers)
        
    if request.method == 'PUT':
        myDict = request.json
        try:
            idToUpdate = myDict['id']
            del myDict['id']
        except: 
            return 'Be careful you forgot to enter the id of the row to update, please add an id and try again !!'

        if len(myDict.values())== 0 :
            return "Be careful you forgot to enter the new data for update!!"

        to_update = []
        to_update.append("update peaks_locations set " + ", ".join("%s = '%s'" % (k, v) for k, v in myDict.items()) + " where id = %s" % idToUpdate)
        cursor.execute(to_update[0])
        conn.commit()
        response=jsonify(success=True)
        print(response)
            
    if request.method == 'DELETE':
        
        if(request.json['id'] == '') :
            return 'Be careful you forgot to enter the id of the row to delete, please add an id and try again !!'
        idToDelete = request.json['id']
        cursor.execute("delete from peaks_locations where id = %s", (idToDelete,))
        conn.commit()
        response = jsonify(success=True)

    return response
 
# conn.close() 


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host = '0.0.0.0')
