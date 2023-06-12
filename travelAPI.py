import mysql.connector
from config import USER, PASSWORD, HOST 

class dbConnectError(Exception):
    pass 

def connectToDB(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# Add user to users table
def addUser(newUser): 
    dbName = 'travelr'
    dbConnection = connectToDB(dbName)
    cur = dbConnection.cursor()
    query = """
    INSERT INTO users (firstName, lastName, email, password) VALUES (%s, %s, %s , %s);
    """ 
    values = (
        newUser['firstName'], 
        newUser['lastName'], 
        newUser['email'],
        newUser['password']
    )
    cur.execute(query, values)
    dbConnection.commit()
    last_row_id = cur.lastrowid
    cur.close()
    return selectUser(last_row_id) 


# Select one user from the db
def selectUser(userID): 
    dbName = 'travelr'
    dbConnection = connectToDB(dbName)
    cur = dbConnection.cursor()
    query = """
    SELECT userID, firstName, lastName, email, password FROM users 
    WHERE userID = %s
    """
    cur.execute(query, (userID,))
    user = cur.fetchone()
    if user is None:
        return None
    
    selectedUser = {
        'userID': user[0],
        'firstName': user[1],
        'lastName': user[2],
        'email': user[3],
    }
    return selectedUser

# Add place to destinations table
def addDestination(newDestination): 
    dbName = 'travelr'
    dbConnection = connectToDB(dbName)
    cur = dbConnection.cursor()
    query = """
    INSERT INTO destinations (destinationName) VALUES (%s);    
    """ 
    values = (
        newDestination['destinationName'],
    )
    cur.execute(query, values)
    dbConnection.commit()
    last_row_id = cur.lastrowid
    cur.close()
    return searchDestination(last_row_id) 

# Select all destinations by user: 

def getDestinations(): 
    destinations = []
    dbName = 'travelr'
    dbConnection = connectToDB(dbName)
    cur = dbConnection.cursor()
    query = """
    SELECT destinationID, destinationName, status FROM destinations 
    WHERE userID = 1;
    """
    cur.execute(query)
    
    for (destinationID, destinationName, status) in cur:
        destinations.append(
            {'destinationID': destinationID,
             'destinationName': destinationName,
             'status': status
            }
        )
    
    return destinations

#Select one destination 

def searchDestination(destinationID): 
    dbName = 'travelr'
    db_connection = connectToDB(dbName)
    cur = db_connection.cursor()
    query = """
    SELECT destinationID, destinationName, status, userID FROM destinations
    WHERE destinationID = %s AND userID = 1; 
    """
    
    cur.execute(query, (destinationID,))
    destination = cur.fetchone()
    if destination is None:
        return None
    
    selectedDestination = {
        'destinationID': destination[0],
        'destinationName': destination[1],
        'status': destination[2],
        'userID': destination[3]
    }

    return selectedDestination