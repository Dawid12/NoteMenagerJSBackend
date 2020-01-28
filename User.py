from Model import Model
from sqlalchemy import Column, BigInteger, String

class User(Model):
   __tablename__ = 'user'
   UserId = Column('id',BigInteger, primary_key=True)
   Login = Column("login",String(50))
   Password = Column("password",String(256))
   Salt = Column("salt",String(256))
   Email = Column("email",String(256))
   
   @staticmethod
   def get(params):
       newUser = User()
       if "UserId" in params:
        newUser.UserId = params['UserId']
       if "Login" in params:
        newUser.Login = params['Login']
       if "Password" in params:
        newUser.Password = params['Password']
       if "Salt" in params:
        newUser.Salt = params['Salt']
       if "Email" in params:
        newUser.Email = params['Email']
       return newUser
       
   def to_dict(self):
        result = {}
        result['UserId']=self.UserId
        result['Login']=self.Login
        result['Password']=self.Password
        result['Email']=self.Email
        return result