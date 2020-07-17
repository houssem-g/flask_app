"""This is flask api which allow send data from psqgl to frontend"""
import json
import psycopg2
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

#instance flask
APP = Flask(__name__)
CORS(APP)
CONN = psycopg2.connect(
    user="postgres", password="root",
    host='localhost', port="5432", database="postgres"
)
CURSOR = CONN.cursor()
@APP.route('/')
def main():
    return render_template('index.html')
@APP.route('/mapView')
def mapview():
    return render_template('viewMap.html')

@APP.route('/help')
def func_documentation():
    documentation = open('api_doc.txt', 'r')
    documentation.close()
    return render_template("api_doc.html")
@APP.route('/readAllTable', methods=['get', 'post', 'put', 'delete'])
def getalldata():
    if request.method == 'GET' and request.args:
        query = (
            "select * from peaks_locations where lat > %s and "
            "lon > %s and lat < %s and lon < %s"
        )
        CURSOR.execute(query,
                       (
                           request.args['minLat'], request.args['minLon'],
                           request.args['maxLat'], request.args['maxLon']
                       )
                      )

        data = CURSOR.fetchall()
        dictionary = []
        for liste in data:
            newvalues = {
                "latitude" : liste[0], "longitude" : liste[1],
                "altitude" : liste[2], "name" : liste[3]
            }
            dictionary.append(newvalues)
        response = APP.response_class(
            response=json.dumps(dictionary),
            status=200,
            content_type='application/json'
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    elif request.method == 'GET' and not request.args:
        query = "select * from peaks_locations"
        CURSOR.execute(query)
        data = CURSOR.fetchall()
        dictionary = []
        for liste in data:
            newvalues = {
                "id": liste[0], "latitude" : liste[1],
                "longitude" : liste[2], "altitude" : liste[3], "name" : liste[4]
            }

            dictionary.append(newvalues)
        response = APP.response_class(
            response=json.dumps(dictionary),
            status=200,
            content_type='application/json'
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    elif request.method == 'POST':
        data_post = request.json
        if len(data_post.values()) != 4:
            return "please fill all fields"
        latitude = request.json['lat']
        longitude = request.json['lon']
        altitude = request.json['altitude']
        nom = request.json['name']
        query = "INSERT INTO peaks_locations (lat, lon, altitude, name) VALUES (%s, %s, %s, %s);"
        CURSOR.execute(query, (latitude, longitude, altitude, nom))
        CONN.commit()
        response = jsonify(success=True)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    elif request.method == 'PUT':
        my_dict = request.json
        try:
            id_to_update = my_dict['id']
            del my_dict['id']
        except:
            return """Be careful you forgot to enter the id of the
            row to update, please add an id and try again !!"""
        if not my_dict.values():
            return "Be careful you forgot to enter the new data for update!!"
        to_update = []
        to_update.append(
            "update peaks_locations set "
            + ", ".join("%s = '%s'" % (k, v) for k, v in my_dict.items())
            + " where id = %s" % id_to_update)
        CURSOR.execute(to_update[0])
        CONN.commit()
        response = jsonify(success=True)
    if request.method == 'DELETE':
        if request.json['id'] == '':
            return """Be careful you forgot to enter the id of the row to delete,
            please add an id and try again !!"""
        to_delete_id = request.json['id']
        CURSOR.execute("delete from peaks_locations where id = %s", (to_delete_id,))
        CONN.commit()
        response = jsonify(success=True)
    return response
# CONN.close()


if __name__ == "__main__":
    APP.run(debug=True)
