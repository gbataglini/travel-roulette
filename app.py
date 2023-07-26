from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from travelAPI import addUser, selectUser, addDestination, getDestinations, searchDestination, getRandomDestination, newDestinationStatus

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def greet(): 
    return 'Hi! :)'


@app.route('/api/v1/users', methods = ['POST'])
def newUser():
    new_user = request.get_json()
    user = addUser(new_user)
    return user


@app.route('/api/v1/users/<int:userID>', methods = ['GET'])
def getUser(userID):
     user = selectUser(userID)
     return jsonify(user)


@app.route('/api/v1/destinations/<int:destinationID>', methods=['GET'])
def getDestination(destinationID): 
    destination = searchDestination(destinationID)
    return jsonify(destination)


@app.route('/api/v1/destinations', methods=['GET'])
def allDestinations():
    destinations = getDestinations()
    return jsonify(destinations)


@app.route('/api/v1/destinations', methods=['POST'])
@cross_origin(origins=['*'])
def newDestination():
    new_destination = request.get_json()
    destination = addDestination(new_destination)
    return destination

@app.route('/api/v1/destinations/random', methods=['GET'])
def randomPick(): 
    destination = getRandomDestination()
    return jsonify(destination)

@app.route('/api/v1/destinations/<int:destinationID>', methods=['PATCH'])
def newStatus(destinationID): 
    reqBody = request.get_json()
    currentStatus = newDestinationStatus(reqBody, destinationID)
    return currentStatus

if __name__ == '__main__':
    app.run(debug=True, port=5001)