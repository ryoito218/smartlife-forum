from sqlalchemy import Column, Integer, String, Text, DateTime, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import pickle

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False, index=True)
    content = Column(Text, nullable=False)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    vector = Column(LargeBinary)

    def set_vector(self, vector):
        self.vector = pickle.dumps(vector)
    
    def get_vector(self):
        return pickle.loads(self.vector)