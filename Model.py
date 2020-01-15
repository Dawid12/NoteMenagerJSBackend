from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

def to_dict(self):
    result = {}
    result['sampleKey']='sampleValue'
    return result

Model.to_dict = to_dict