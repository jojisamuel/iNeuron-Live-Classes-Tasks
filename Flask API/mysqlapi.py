from flask import Flask, request, jsonify
import mysql.connector as connection
mydb = connection.connect(user='root', password='admin', host='127.0.0.1')
cursor = mydb.cursor()

q = 'use ineurontask'
cursor.execute(q)

app = Flask(__name__)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        name = request.json['name']
        place = request.json['place']
        q1="INSERT INTO 20augtask VALUES ('%s', '%s')" % (name, place)
        print(q1)
        cursor.execute(q1)
        mydb.commit()
        return jsonify('INSERTED')

@app.route('/update',methods=['GET' , 'POST'])
def update():
    if (request.method == 'POST'):
        name = request.json['name']
        place = request.json['place']
        q1 = "update 20augtask set place = '%s' where name = ('%s')" % (place,name)
        print(q1)
        cursor.execute(q1)
        mydb.commit()
        return jsonify(('RECORD Updated'))

@app.route('/delete',methods=['GET' , 'POST'])
def delete():
    if (request.method == 'POST'):
        name = request.json['name']
        q1 = "delete FROM 20augtask where name = ('%s')" % (name)
        cursor.execute(q1)
        mydb.commit()
        return jsonify(('RECORD DELETED'))

@app.route('/select',methods=['GET' , 'POST'])
def select():
     if (request.method == 'POST'):
        name = request.json['name']
        q1 = "SELECT * FROM 20augtask where name = ('%s')" % (name)
        cursor.execute(q1)
        rv = cursor.fetchall()
        return jsonify(rv)

if __name__ == '__main__':
    app.run()