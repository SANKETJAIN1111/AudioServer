from fastapi import APIRouter
from fastapi import Body,FastAPI, Depends, status, HTTPException,Query,Path
from uuid import UUID

from datetime import datetime, time, timedelta
from typing import Optional
from typing import List,Union,Any,Dict
from pydantic import BaseModel
from .. import schemas, models, database
from AudioServer.Repository import audiofileRepository
from ..database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session

router= APIRouter(
    prefix="/AudioTypes",
    tags=["AudioTypes"],
    dependencies=[Depends(database.get_db)])



# Get ApI
@router.get("/{model_name}/{id}",status_code=status.HTTP_200_OK )
def Get_API(id,model_name: schemas.ModelName,db:Session=Depends(database.get_db)):
    return audiofileRepository.get_data(db=db,id=id,model_name= model_name)

# post
@router.post("/{types}/Song", response_model=Union[schemas.Item, schemas.Song],status_code=status.HTTP_200_OK) 
def create_song(types: schemas.ModelName, item: schemas.CreateSongs, db: Session = Depends(get_db)):
    data = audiofileRepository.create_song_item(db=db,item=item,types=types)
    return data

@router.post("/{types}/Audiobook", response_model=Union[schemas.ItemAudiobook, schemas.Audiobook],status_code=status.HTTP_200_OK)
def create_audiobook(types: schemas.ModelName, item: schemas.CreateAudiobook, db: Session = Depends(get_db)):
    data = audiofileRepository.create_audiobook_item(db=db,item=item,types=types)
    return data

@router.post("/{types}/Podcast", response_model=Union[schemas.ItemPodcast, schemas.Podcast],status_code=status.HTTP_200_OK)
def create_podcast(types: schemas.ModelName, item: schemas.CreatePodcast, db: Session = Depends(get_db)):
    data = audiofileRepository.create_podcast_item(db=db,item=item,types=types)
    return data
        
# Get ApI
@router.get("/{model_name}/{id}",status_code=status.HTTP_200_OK)
def Get_API(id,model_name: schemas.ModelName,db:Session=Depends(get_db)):
    return audiofileRepository.get_data(db=db,id=id,model_name= model_name)

#Put ApI Songs
@router.put('/Songs/{id}', status_code=status.HTTP_200_OK)
def Update_Song(id,model_name: schemas.ModelName,request:schemas.Song, db:Session=Depends(get_db)):
    return audiofileRepository.update_Song(db=db,id=id,model_name=model_name,request=request)

#Put ApI Audiobook
@router.put('/Audiobook/{id}', status_code=status.HTTP_200_OK)
def Update_Audiobook(id,model_name: schemas.ModelName,request:schemas.Audiobook, db:Session=Depends(get_db)):
    return audiofileRepository.update_Audiobook(db=db,id=id,model_name=model_name,request=request)

#Put ApI Podcast
@router.put('/Podcast/{id}', status_code=status.HTTP_200_OK)
def Update_Podcast(id,model_name: schemas.ModelName,request:schemas.Podcast, db:Session=Depends(get_db)):  
    return audiofileRepository.update_Podcast(db=db,id=id,model_name=model_name,request=request)

# Delete API
@router.delete('/{model_name}/{id}' ,status_code=status.HTTP_200_OK)
def Delete_API(id,model_name: schemas.ModelName, db:Session=Depends(get_db)):
    data = audiofileRepository.delete_data(db=db,id=id,model_name=model_name)
    return data