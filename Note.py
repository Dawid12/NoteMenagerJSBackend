from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime

class Note(Model):
   __tablename__ = 'note'
   noteId = Column(BigInteger, primary_key=True)
   taskId = Column(BigInteger, nullable=False)
   userId = Column(BigInteger, nullable=False)
   noteText = Column(String(256))
   masterNoteId = Column(BigInteger, nullable=False)
   title = Column(String(256))
   creationDate = Column(DateTime)
   editionDate = Column(DateTime)
   