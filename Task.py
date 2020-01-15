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
   