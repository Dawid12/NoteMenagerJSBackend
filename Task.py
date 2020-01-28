from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime
from common import getIntDate, convertToDate

class Task(Model):
   __tablename__ = 'task'
   TaskId = Column("taskId",BigInteger, primary_key=True)
   UserId = Column("userId",BigInteger, nullable=False)
   TaskText = Column("taskText",String(256))
   Title = Column("title",String(256))
   CreationDate = Column("creationDate",DateTime)
   EditionDate = Column("editionDate",DateTime)
   TaskStatus = Column("taskStatus",BigInteger, nullable=False)
   MasterTaskId = Column("masterTaskId",BigInteger)
   
   @staticmethod
   def get(params):
       newTask = Task()
       if "TaskId" in params:
        newTask.TaskId = params['TaskId']
       if "UserId" in params:
        newTask.UserId = params['UserId']
       if "TaskText" in params:
        newTask.TaskText = params['TaskText']
       if "Title" in params:
        newTask.Title = params['Title']
       if "CreationDate" in params:
        newTask.CreationDate = convertToDate(params['CreationDate'])
       if "EditionDate" in params:
        newTask.EditionDate = convertToDate(params['EditionDate'])
       if "TaskStatus" in params:
        newTask.TaskStatus = params['TaskStatus']
       if "MasterTaskId" in params:
        newTask.MasterTaskId = params['MasterTaskId']
       return newTask
       
   def to_dict(self):
        result = {}
        result['TaskId']=self.TaskId
        result['UserId']=self.UserId
        result['TaskText']=self.TaskText
        result['Title']=self.Title
        result['CreationDate']=str(getIntDate(self.CreationDate))
        result['EditionDate']=str(getIntDate(self.EditionDate))
        result['TaskStatus']=self.TaskStatus
        result['MasterTaskId']=self.MasterTaskId
        result['DeadlineDate']=None
        return result