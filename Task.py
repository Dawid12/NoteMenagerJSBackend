from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime

class Task(Model):
   __tablename__ = 'task'
   taskId = Column(BigInteger, primary_key=True)
   userId = Column(BigInteger, nullable=False)
   taskText = Column(String(256))
   title = Column(String(256))
   creationDate = Column(DateTime)
   editionDate = Column(DateTime)
   taskStatus = Column(BigInteger, nullable=False)
   masterTaskId = Column(BigInteger, nullable=False)
   
   @staticmethod
   def get(params):
       newTask = User()
       if "taskId" in params:
        newTask.taskId = params['taskId']
       if "userId" in params:
        newTask.userId = params['userId']
       if "taskText" in params:
        newTask.taskText = params['taskText']
       if "title" in params:
        newTask.title = params['title']
       if "creationDate" in params:
        newTask.creationDate = params['creationDate']
       if "editionDate" in params:
        newTask.editionDate = params['editionDate']
       if "taskStatus" in params:
        newTask.taskStatus = params['taskStatus']
       if "masterTaskId" in params:
        newTask.masterTaskId = params['masterTaskId']
       return newTask
       
   def to_dict(self):
        result = {}
        result['taskId']=self.taskId
        result['userId']=self.userId
        result['taskText']=self.taskText
        result['title']=self.title
        result['creationDate']=self.creationDate
        result['editionDate']=self.editionDate
        result['taskStatus']=self.taskStatus
        result['masterTaskId']=self.masterTaskId
        return result