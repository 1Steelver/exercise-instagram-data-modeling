import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    first_name = Column(String(15))
    last_name = Column(String(15))
    email = Column(String(90))
    password = Column(String(100))

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))

class Post(Base):
    __tablename__= "post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__= "comment"

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(2200))
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))

class Media(Base):
    __tablename__="media"
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    url = Column(String(2000))
    post_id = Column(Integer, ForeignKey("post.id"))        


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e