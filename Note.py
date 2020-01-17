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
   
   @staticmethod
   def get(params):
       newNote = Note()
       if "noteId" in params:
        newNote.noteId = params['noteId']
       if "taskId" in params:
        newNote.taskId = params['taskId']
       if "userId" in params:
        newNote.userId = params['userId']
       if "noteText" in params:
        newNote.noteText = params['noteText']
       if "title" in params:
        newNote.title = params['title']
       if "creationDate" in params:
        newNote.creationDate = params['creationDate']
       if "editionDate" in params:
        newNote.editionDate = params['editionDate']
       if "masterNoteId" in params:
        newNote.masterNoteId = params['masterNoteId']
       return newNote
       
   def to_dict(self):
        result = {}
        result['noteId']=self.noteId
        result['taskId']=self.taskId
        result['userId']=self.userId
        result['noteText']=self.noteText
        result['title']=self.title
        result['creationDate']=self.creationDate
        result['editionDate']=self.editionDate
        result['masterNoteId']=self.masterNoteId
        return result