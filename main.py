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
    user = User(request.json)
    result = get_session().query(Note).filter_by(userId = user.id).all() 
    response = []
    if len(result) > 0:
        for n in result:
            response.append(n.to_dict())
    return json.dumps(response)
    
@app.route('/createNote/', methods=['POST'])
def createNote():
    note = Note(request.json)
    session = get_session()
    lastNote = session.guery(Note).odrer_by(Note.noteId).last()
    note.id = 1 if lastNote == None else lastNote.id + 1
    session.add(note)
    session.flush()
    return json.dumps(note.to_dict())
    
@app.route('/saveNote/', methods=['POST'])
def saveNote():
    note = Note(request.json)
    session = get_session()
    found = session.guery(Note).filter_by(noteId = note.noteId).first()
    if found != None:
        found.masterNoteId = note.masterNoteId
        found.taskId = note.taskId
        found.title = note.title
        found.noteText = note.noteText
        found.creationDate = note.creationDate
        found.editionDate = note.editionDate
        session.flush()
        return True
    return False
    
@app.route('/deleteNotes/', methods=['POST'])
def deleteNotes():
    session = get_session()
    for n in request.json:
        note = Note(n)
        found = session.guery(Note).filter_by(noteId = note.noteId).first()
        if found != None:
            session.delete(found)
    session.flush()
    return True
    
@app.route('/userTasks/', methods=['POST'])
def usertasks():
    user = User(request.json)
    result = get_session().query(Task).filter_by(userId = user.id).all() 
    response = []
    if len(result) > 0:
        for n in result:
            response.append(n.to_dict())
    return json.dumps(response)
    
@app.route('/createTask/', methods=['POST'])
def createTask():
    task = Task(request.json)
    session = get_session()
    lastTask = session.guery(Task).odrer_by(Task.taskId).last()
    task.id = 1 if lastTask == None else lasttask.id + 1
    session.add(task)
    session.flush()
    return json.dumps(task.to_dict())
    
@app.route('/deleteTask/', methods=['POST'])
def deleteTask():
    session = get_session()
    for t in request.json:
        task = Task(t)
        found = session.guery(Task).filter_by(taskId = task.taskId).first()
        if found != None:
            session.delete(found)
    session.flush()
    return True
    
@app.route('/updateTask/', methods=['POST'])
def updateTask():
    task = Task(request.json)
    session = get_session()
    found = session.guery(Task).filter_by(taskId = task.taskId).first()
    if found != None:
        found.masterTaskId = task.masterTaskId
        found.title = task.title
        found.taskText = task.taskText
        found.creationDate = task.creationDate
        found.editionDate = task.editionDate
        found.taskStatus = task.taskStatus
        session.flush()
        return True
    return False
    
@app.route('/getTaskStatuses/', methods=['POST'])
def getTaskStatuses():
    result = get_session().query(TaskStatus).all() 
    response = []
    if len(result) > 0:
        for s in result:
            response.append(s.to_dict())
    return json.dumps(response)
    
if __name__ == '__main__':
    app.run(debug=True)
