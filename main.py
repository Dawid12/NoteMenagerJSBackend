from flask import Flask, request, Response
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
        return Response(json.dumps(response), mimetype='application/json')
    return Response(json.dumps(User().to_dict()), mimetype='application/json')

@app.route('/getUser/', methods=['POST'])
def getUser():
    user = User.get(request.json)
    found = get_session().query(User).filter_by(login = user.login).first()
    if found != None:
        salted = generate_salted_hash(user.password, found.salt)
        if salted == found.password:
            return Response(json.dumps(found.to_dict()), mimetype='application/json')
    return Response(json.dumps(User().to_dict()), mimetype='application/json')
    
@app.route('/createUser/', methods=['POST'])
def createUser():
    user = User.get(request.json)
    user.salt = get_salt()
    user.password = generate_salted_hash(user.password, user.salt)
    session = get_session()
    session.add(user)
    user.userId = session.query(User).filter_by(login = user.login).first().userId
    session.flush()
    return Response(json.dumps(user.to_dict()), mimetype='application/json')
    
@app.route('/userNotes/', methods=['POST'])
def userNotes():
    user = User.get(request.json)
    result = get_session().query(Note).filter_by(userId = user.userId).all() 
    response = []
    if len(result) > 0:
        for n in result:
            response.append(n.to_dict())
    return Response(json.dumps(response), mimetype='application/json')
    
@app.route('/createNote/', methods=['POST'])
def createNote():
    note = Note.get(request.json)
    session = get_session()
    lastNote = session.query(Note).order_by(Note.noteId.desc()).first()
    note.noteId = 1 if lastNote == None else lastNote.noteId + 1
    try:
        session.add(note)
        session.flush()
    except:
        note = Note()
    return Response(json.dumps(note.to_dict()), mimetype='application/json')
    
@app.route('/saveNote/', methods=['POST'])
def saveNote():
    note = Note.get(request.json)
    session = get_session()
    found = session.query(Note).filter_by(noteId = note.noteId).first()
    if found != None:
        found.masterNoteId = note.masterNoteId
        found.taskId = note.taskId
        found.title = note.title
        found.noteText = note.noteText
        found.creationDate = note.creationDate
        found.editionDate = note.editionDate
        session.flush()
        return Response(json.dumps(True), mimetype='application/json')
    return Response(json.dumps(False), mimetype='application/json')
    
@app.route('/deleteNotes/', methods=['POST'])
def deleteNotes():
    session = get_session()
    for n in request.json:
        note = Note.get(n)
        found = session.query(Note).filter_by(noteId = note.noteId).first()
        if found != None:
            session.delete(found)
    session.flush()
    return Response(json.dumps(True), mimetype='application/json')
    
@app.route('/userTasks/', methods=['POST'])
def usertasks():
    user = User.get(request.json)
    result = get_session().query(Task).filter_by(userId = user.userId).all() 
    response = []
    if len(result) > 0:
        for n in result:
            response.append(n.to_dict())
    return Response(json.dumps(response), mimetype='application/json')
    
@app.route('/createTask/', methods=['POST'])
def createTask():
    task = Task.get(request.json)
    session = get_session()
    lastTask = session.query(Task).order_by(Task.taskId.desc()).first()
    task.taskId = 1 if lastTask == None else lastTask.taskId + 1
    try:
        session.add(task)
        session.flush()
    except:
        task = Task()
    return Response(json.dumps(task.to_dict()), mimetype='application/json')
    
@app.route('/deleteTask/', methods=['POST'])
def deleteTask():
    session = get_session()
    for t in request.json:
        task = Task.get(t)
        found = session.query(Task).filter_by(taskId = task.taskId).first()
        if found != None:
            session.delete(found)
    session.flush()
    return Response(json.dumps(True), mimetype='application/json')
    
@app.route('/updateTask/', methods=['POST'])
def updateTask():
    task = Task.get(request.json)
    session = get_session()
    found = session.query(Task).filter_by(taskId = task.taskId).first()
    if found != None:
        found.masterTaskId = task.masterTaskId
        found.title = task.title
        found.taskText = task.taskText
        found.creationDate = task.creationDate
        found.editionDate = task.editionDate
        found.taskStatus = task.taskStatus
        session.flush()
        return Response(json.dumps(True), mimetype='application/json')
    return Response(json.dumps(False), mimetype='application/json')
    
@app.route('/getTaskStatuses/', methods=['POST'])
def getTaskStatuses():
    result = get_session().query(TaskStatus).all() 
    response = []
    if len(result) > 0:
        for s in result:
            response.append(s.to_dict())
    return Response(json.dumps(response), mimetype='application/json')
    
if __name__ == '__main__':
    app.run(debug=True)
