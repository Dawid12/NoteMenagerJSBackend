from Model import Model
from sqlalchemy import Column, BigInteger, String

class User(Model):
   __tablename__ = 'user'
   id = Column(BigInteger, primary_key=True)
   login = Column(String(50))
   password = Column(String(256))
   salt = Column(String(256))
   email = Column(String(256))
   