CREATE DATABASE travelr; 

USE travelr;

CREATE TABLE users (
userID INT NOT NULL AUTO_INCREMENT,
firstName VARCHAR(50) NOT NULL, 
lastName VARCHAR(100) NOT NULL, 
email VARCHAR(100) NOT NULL UNIQUE, 
password VARCHAR(50) NOT NULL, 
PRIMARY KEY (UserID)
);

CREATE TABLE destinations (
destinationID INT NOT NULL AUTO_INCREMENT, 
destinationName VARCHAR(200) NOT NULL,
userID INT NOT NULL DEFAULT 1, 
status ENUM('not visited', 'visited', 'going') NOT NULL DEFAULT 'not visited', 
FOREIGN KEY (userID) REFERENCES users(userID), 
PRIMARY KEY (destinationID)
);