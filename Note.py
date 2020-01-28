from Model import Model
from sqlalchemy import Column, BigInteger, String, DateTime
from common import getIntDate, convertToDate

class Note(Model):
   __tablename__ = 'note'
   NoteId = Column("noteId",BigInteger, primary_key=True)
   TaskId = Column("taskId",BigInteger)
   UserId = Column("userId",BigInteger, nullable=False)
   NoteText = Column("noteText",String(256))
   MasterNoteId = Column("masterNoteId",BigInteger)
   Title = Column("title",String(256))
   CreationDate = Column("creationDate",DateTime)
   EditionDate = Column("editionDate",DateTime)
   
   @staticmethod
   def get(params):
       newNote = Note()
       if "NoteId" in params:
        newNote.NoteId = params['NoteId']
       if "TaskId" in params:
        newNote.TaskId = params['TaskId']
       if "UserId" in params:
        newNote.UserId = params['UserId']
       if "NoteText" in params:
        newNote.NoteText = params['NoteText']
       if "Title" in params:
        newNote.Title = params['Title']
       if "CreationDate" in params:
        newNote.CreationDate = convertToDate(params['CreationDate'])
       if "EditionDate" in params:
        newNote.EditionDate = convertToDate(params['EditionDate'])
       if "MasterNoteId" in params:
        newNote.MasterNoteId = params['MasterNoteId']
       return newNote
       
   def to_dict(self):
        result = {}
        result['NoteId']=self.NoteId
        result['TaskId']=self.TaskId
        result['UserId']=self.UserId
        result['NoteText']=self.NoteText
        result['Title']=self.Title
        result['CreationDate']=str(getIntDate(self.CreationDate))
        result['EditionDate']=str(getIntDate(self.EditionDate))
        result['MasteNoteId']=self.MasterNoteId
        return result