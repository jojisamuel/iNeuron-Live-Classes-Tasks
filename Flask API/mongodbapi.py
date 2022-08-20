import pymongo
from flask import Flask, request, jsonify

client = pymongo.MongoClient("mongodb+srv://jojis:*******@cluster0.wj6gl.mongodb.net/?retryWrites=true&w=majority")
mydb = client['ineuron']
mycol = mydb['20Augtask']

app = Flask(__name__)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if (request.method == 'POST'):
        name = request.json['name']
        place = request.json['place']
        record = {'name': name, 'place': place}
        print(record)
        mycol.insert_one(record)
        resp = jsonify('User added successfully!')
        return resp

@app.route('/update', methods=['GET', 'POST'])
def update():
    if (request.method == 'POST'):
        name = request.json['name']
        place = request.json['place']
        myquery = {"name": name}
        newvalues = {"$set": {"place": place}}
        mycol.update_one(myquery, newvalues)
        resp = jsonify('User updated successfully!')
        return resp


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'POST'):
        name = request.json['name']
        record = {'name': name}
        mycol.delete_one(record)
        resp = jsonify('User deleted successfully!')
        return resp

@app.route('/select', methods=['GET', 'POST'])
def findAll():
	query = mycol.find()
	output = {}
	i = 0
	for x in query:
		output[i] = x
		output[i].pop('_id')
		i += 1
	return jsonify(output)


if __name__ == '__main__':
    app.run()
