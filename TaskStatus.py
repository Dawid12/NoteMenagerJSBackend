from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime

class TaskStatus(Model):
   __tablename__ = 'taskStatusDict'
   statusId = Column(BigInteger, primary_key=True)
   name = Column('status',String(256), nullable=False)
   
   @staticmethod
   def get(params):
       newStatus = TaskStatus()
       if "statusId" in params:
        newStatus.statusId = params['statusId']
       if "name" in params:
        newStatus.name= params['name']
       return newStatus
       
   def to_dict(self):
        result = {}
        result['statusId']=self.statusId
        result['name']=self.name
        return result