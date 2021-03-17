from sqlalchemy import Column, Integer,String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from typing import List
from .database import Base
from datetime import datetime 

class Songs(Base):
    __tablename__= 'Songs'
    id=Column(Integer,primary_key=True,unique=True,index=True)
    Name_of_the_song=Column(String(100))
    Duration_in_number_of_seconds=Column(Integer)
    Uploaded_time=Column(String)
    typedata= Column(String,ForeignKey('AudioType.types'))
    types = relationship("AudioTypes", back_populates="Audio")


class Podcast(Base):
    __tablename__= 'Podcasts'
    id=Column(Integer,primary_key=True,unique=True,index=True)
    Name_of_the_podcast=Column(String(100),index=True)
    Duration_in_number_of_seconds=Column(Integer)
    Uploaded_time=Column(Integer,index=True)
    Host=Column(String(100),index=True)
    Participants=Column(String,index=True)
    typedata= Column(String,ForeignKey('AudioType.types'))
    types = relationship("AudioTypes", back_populates="Podcasts")

class Audiobook(Base):
    __tablename__= 'Audiobooks'
    id=Column(Integer,primary_key=True,unique=True,index=True)
    Title_of_the_audiobook=Column(String(100),index=True)
    Author_of_the_title=Column(String(100),index=True)
    Narretor=Column(String(100),index=True)
    Duration_in_number_of_seconds=Column(Integer)
    Uploaded_time=Column(String,index=True)
    typedata= Column(String,ForeignKey('AudioType.types'))
    types = relationship("AudioTypes", back_populates="Audiobooks")


class AudioTypes(Base):
    __tablename__= 'AudioType'
    id=Column(Integer,unique=True,index=True)
    types=Column(String,primary_key=True,unique=True,index=True)
    metaData=Column(String)
    Audio = relationship('Songs',back_populates="types")
    Audiobooks = relationship('Audiobook',back_populates="types")
    Podcasts = relationship('Podcast',back_populates="types")