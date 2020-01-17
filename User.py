from Model import Model
from sqlalchemy import Column, BigInteger, String

class User(Model):
   __tablename__ = 'user'
   userId = Column('id',BigInteger, primary_key=True)
   login = Column(String(50))
   password = Column(String(256))
   salt = Column(String(256))
   email = Column(String(256))
   
   @staticmethod
   def get(params):
       newUser = User()
       if "userId" in params:
        newUser.userId = params['userId']
       if "login" in params:
        newUser.login = params['login']
       if "password" in params:
        newUser.password = params['password']
       if "salt" in params:
        newUser.salt = params['salt']
       if "email" in params:
        newUser.email = params['email']
       return newUser
       
   def to_dict(self):
        result = {}
        result['userId']=self.userId
        result['login']=self.login
        result['password']=self.password
        result['email']=self.email
        return result