from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime

class TaskStatus(Model):
   __tablename__ = 'taskStatusDict'
   statusId = Column(BigInteger, primary_key=True)
   status = Column(String(256), nullable=False)
   
   @staticmethod
   def get(params):
       newStatus = User()
       if "statusId" in params:
        newStatus.statusId = params['statusId']
       if "status" in params:
        newStatus.status= params['status']
       return newStatus
       
   def to_dict(self):
        result = {}
        result['statusId']=self.statusId
        result['status']=self.status
        return result