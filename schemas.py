from pydantic import BaseModel
from fastapi import Body, Query
from datetime import datetime,date
from typing import List,Optional,Dict
from enum import Enum
now = datetime.now()

class Song(BaseModel):
    Name_of_the_song:str =Query(None, max_length=100)
    Duration_in_number_of_seconds:Optional[int]
    Uploaded_time:Optional[datetime]=Body(None)
    class Config():
        orm_mode = True

class Podcast(BaseModel):
    Name_of_the_podcast:str = Query(None, max_length=100)
    Duration_in_number_of_seconds:Optional[int]
    Uploaded_time:Optional[date]=Body(None)
    Host:str =Query(None, max_length=100)
    Participants:Optional[str] =Query(None, max_length=100)
    class Config():
        orm_mode = True
    
class Audiobook(BaseModel):
    Title_of_the_audiobook:str =Query(None, max_length=100)
    Author_of_the_title:str =Query(None, max_length=100)
    Narretor:str=Query(None, max_length=100)
    Duration_in_number_of_seconds:Optional[int]
    Uploaded_time:Optional[datetime]=Body(None)
    class Config():
        orm_mode = True
class Item(Song):
    id: int
    typedata: str
    class Config():
        orm_mode = True
class ItemPodcast(Podcast):
    id: int
    typedata: str
    class Config():
        orm_mode = True
class ItemAudiobook(Audiobook):
    id: int
    typedata: str
    class Config():
        orm_mode = True

class CreateSongs(Song):
    pass
class CreatePodcast(Podcast):
    pass
class CreateAudiobook(Audiobook):
    pass
class ModelName(str,Enum):
    # TypeItem=str
    Song = "Song"
    Audiobook = "Audiobook"
    Podcast = "Podcast"
    def ModelName(string:str):  
        if string==Song:
            return CreateSongs
        if string==Podcsat:
            return CreatePodcast
        if string==Audiobook:
            return CreateAudiobook

        
    
class TypeTable(BaseModel):
    typedata: str

class ShowSongs(BaseModel):
    Name_of_the_song:str
    Duration_in_number_of_seconds:Optional[datetime]=Body(None)
    Uploaded_time:Optional[datetime]=Body(None) 
    Created_date:Optional[datetime]=Body(None)
class Config():
    orm_mode = True



class common():
    def CurrentDate(Uploaded_time):
        currentTime = datetime.now()
        updateTime = Uploaded_time
        print(currentTime)
        print(updateTime)
        if updateTime >= currentTime:
            return updateTime
        else:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Date Should Be Current Date not Previous Date")
        return { "Expected Current Date":currentTime, "Actual Date" : updateTime }
        
    def Duration(Duration_in_number_of_seconds):
        if "-" in Duration_in_number_of_seconds:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Duration Should be Positive")
       



