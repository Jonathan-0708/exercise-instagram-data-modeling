import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR,Enum,Date,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column( String(15), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(VARCHAR(50), nullable=False,primary_key=True,unique=True)
    date_of_birth = Column(Date,nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    publication_date = Column(DateTime, nullable=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(VARCHAR(250),nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer,ForeignKey('post.id'))
    post = relationship(Post)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    follower = relationship(Follower)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum,nullable=False)
    ulr = Column(String(250), nullable=False, unique=True)
    post_id = Column(Integer,ForeignKey('post.id'))
    post = relationship(Post)

class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer,ForeignKey('post.id'))
    post = relationship(Post)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)   

class Reels(Base):
    __tablename__ = 'reels'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer,ForeignKey('post.id'))
    post = relationship(Post)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)
    stories_id = Column(Integer,ForeignKey('stories.id'))
    stories = relationship(Stories)  

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    follower = relationship(Follower)
    stories_id = Column(Integer,ForeignKey('stories.id'))
    stories = relationship(Stories) 
    reels_id =Column(Integer,ForeignKey('reels.id'))
    reels = relationship(Reels)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e