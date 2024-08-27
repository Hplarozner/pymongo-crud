from flask import Flask, jsonify, request, make_response
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["user_app"]
users = db["users"]

@app.route('/user', methods=['GET'])
@cross_origin()
def get_todos():

    user_list = list(users.find())

    for todo in user_list:
        todo['_id'] = str(todo['_id'])
    
    response = make_response(jsonify(user_list))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000/'
    return jsonify(user_list)

@app.route('/user', methods=['POST'])
def add_todo():
    user = request.json
    users.insert_one(user)
    return jsonify({'message': ' added User successfully'})

@app.route('/user/<string:id>', methods=['PUT'])
@cross_origin()
def update_todo(id):
    # find document id in database
    user = users.find_one({'_id': ObjectId(id)})
   
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    updated_user = request.json
 
    
    # # Remove the _id field if it exists to prevent updating it
    if '_id' in updated_user:
        updated_user.pop('_id')

    users.update_one({'_id': ObjectId(id)}, {'$set': updated_user})
    return jsonify({'message': 'User updated successfully'})

@app.route('/user/<string:id>', methods=['DELETE'])
def delete_todo(id):
    users.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)