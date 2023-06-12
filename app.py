from flask import Flask, jsonify, request
from travelAPI import addUser, selectUser, addDestination, getDestinations, searchDestination

app = Flask(__name__)


@app.route('/')
def greet(): 
    return 'Hi! :)'


@app.route('/users', methods = ['POST'])
def newUser():
    new_user = request.get_json()
    user = addUser(new_user)
    return user


@app.route('/users/<int:userID>', methods = ['GET'])
def getUser(userID):
     user = selectUser(userID)
     return jsonify(user)


@app.route('/destinations/<int:destinationID>', methods=['GET'])
def getDestination(destinationID): 
    destination = searchDestination(destinationID)
    return jsonify(destination)


@app.route('/destinations', methods=['GET'])
def allDestinations():
    destinations = getDestinations()
    return jsonify(destinations)


@app.route('/destinations', methods=['POST'])
def newDestination():
    new_destination = request.get_json()
    destination = addDestination(new_destination)
    return destination


if __name__ == '__main__':
    app.run(debug=True, port=5001)