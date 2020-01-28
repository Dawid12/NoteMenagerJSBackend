from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime

class TaskStatus(Model):
   __tablename__ = 'taskStatusDict'
   StatusId = Column("statusId",BigInteger, primary_key=True)
   Name = Column('status',String(256), nullable=False)
   
   @staticmethod
   def get(params):
       newStatus = TaskStatus()
       if "StatusId" in params:
        newStatus.StatusId = params['StatusId']
       if "Name" in params:
        newStatus.Name= params['Name']
       return newStatus
       
   def to_dict(self):
        result = {}
        result['StatusId']=self.StatusId
        result['Name']=self.Name
        return result