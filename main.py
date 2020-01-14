import psycopg2
import flask
import flask
import json
from flask import Flask
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation

app = Flask(__name__)
    
@app.route('/users/', methods=['GET'])
def users():
    return "Not implemented"    

@app.route('/getUser/', methods=['POST'])
def getUser():
    return "Not implemented"  
    
@app.route('/createUser/', methods=['POST'])
def createUser():
    return "Not implemented" 
    
@app.route('/userNotes/', methods=['POST'])
def userNotes():
    return "Not implemented" 
    
@app.route('/createNote/', methods=['POST'])
def createNote():
    return "Not implemented" 
    
@app.route('/saveNote/', methods=['POST'])
def saveNote():
    return "Not implemented" 
    
@app.route('/deleteNotes/', methods=['POST'])
def deleteNotes():
    return "Not implemented" 
    
@app.route('/userTasks/', methods=['POST'])
def usertasks():
    return "Not implemented" 
    
@app.route('/createTask/', methods=['POST'])
def createTask():
    return "Not implemented" 
    
@app.route('/deleteTask/', methods=['POST'])
def deleteTask():
    return "Not implemented" 
    
@app.route('/updateTask/', methods=['POST'])
def updateTask():
    return "Not implemented" 
    
@app.route('/getTaskStatuses/', methods=['POST'])
def getTaskStatuses():
    return "Not implemented" 
    
if __name__ == '__main__':
    app.run(debug=True)
