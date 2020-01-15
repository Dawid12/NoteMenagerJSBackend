from flask import Flask, request
import json
from User import User
from Task import Task
from Note import Note
from TaskStatus import TaskStatus
from DBContext import get_session, create_all
from common import generate_salted_hash, get_salt

create_all()

app = Flask(__name__)
    
@app.route('/users/', methods=['GET'])
def users():
    result = get_session().query(User).all() 
    response = []
    if len(result) > 0:
        for u in result:
            response.append(u.to_dict())
        return json.dumps(response)
    return json.dumps(User().to_dict())

@app.route('/getUser/', methods=['POST'])
def getUser():
    user = User.get(request.json)
    found = get_session().query(User).filter_by(login = user.login).first()
    if found != None:
        salted = generate_salted_hash(user.password, found.salt)
        if salted == found.password:
            return json.dumps(found.to_dict())
    return json.dumps(User().to_dict())
    
@app.route('/createUser/', methods=['POST'])
def createUser():
    user = User.get(request.json)
    user.salt = get_salt()
    user.password = generate_salted_hash(user.password, user.salt)
    session = get_session()
    session.add(user)
    user.id = session.query(User).filter_by(login = user.login).first().id
    session.flush()
    return json.dumps(user.to_dict())
    
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
