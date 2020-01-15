from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime

class TaskStatus(Model):
   __tablename__ = 'taskStatusDict'
   statusId = Column(BigInteger, primary_key=True)
   status = Column(String(256), nullable=False)
   