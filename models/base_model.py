#!/usr/bin/python3
"""
This is the base class for all models in the project
"""
import uuid
from datetime import datetime


class BaseModel:
   def __init__(self):
       self.id = str(uuid.uuid4()()
 
       self.created_at = datetime.utcnow()
       self.updated_at = datetime.utcnow()
 
   def save (self)
       """
      Updates the updated_at attribute with a new value
       """
       self.updated_at =datetime.utcnow()

   def to_dict(self):
       """

       """
       inst_dict= self.__dict__.copy()
       inst_dict["__class__"] = self.__class__.__name__
       inst_dict["created_at"] =self.created_at.isoformat()
       inst_dict["updated_at"] = self.updated_at.isoformat()

       return inst_dict

   def ___str___(self):
       """
       String representation of the instance class
       """
       class_name = self.__class__.name__
       return f " [{class_name}] ({self.id}) {self.__dict__}"
