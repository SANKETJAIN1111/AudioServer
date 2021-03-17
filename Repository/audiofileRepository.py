from .. import schemas, models
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from fastapi.responses import JSONResponse
from typing import Optional,List
from fastapi import Depends, FastAPI

def create_song_item(db: Session, item: schemas.CreateSongs, types: schemas.ModelName):
    duration = schemas.common.Duration(item.Duration_in_number_of_seconds)
    uploaded_time = schemas.common.CurrentDate(item.Uploaded_time)
    if types==types.Song:
        db_item = models.Songs(Name_of_the_song=item.Name_of_the_song,Duration_in_number_of_seconds=duration,Uploaded_time=uploaded_time,typedata=types)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    if not types==types.Podcast:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Please Choose Song Option, Song Item not Created!!")
    return db_item

def create_podcast_item(db: Session, item: schemas.CreatePodcast, types: schemas.ModelName):
    duration = schemas.common.Duration(item.Duration_in_number_of_seconds)
    uploaded_time = schemas.common.CurrentDate(item.Uploaded_time)
    if types==types.Podcast:
        db_item = models.Podcast(Name_of_the_podcast=item.Name_of_the_podcast,Duration_in_number_of_seconds=duration,Uploaded_time=uploaded_time,Participants=item.Participants,Host=item.Host,typedata=types)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    if not types==types.Podcast:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Please Choose Podcast Option, Song Item not Created!!")
    return db_item

def create_audiobook_item(db: Session, item: schemas.CreateAudiobook, types: schemas.ModelName):
    duration = schemas.common.Duration(item.Duration_in_number_of_seconds)
    uploaded_time = schemas.common.CurrentDate(item.Uploaded_time)
    if types==types.Audiobook:
        db_item = models.Audiobook(Title_of_the_audiobook=item.Title_of_the_audiobook,Author_of_the_title=item.Author_of_the_title,Narretor=item.Narretor,Duration_in_number_of_seconds=duration,Uploaded_time=uploaded_time,typedata=types)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
        if not types==types.Podcast:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Please Choose Audiobook Option, Song Item not Created!!")
    return db_item

def get_data(db:Session,id,model_name: schemas.ModelName):
    if model_name == model_name.Song:
        if not db.query(models.Songs).filter(models.Songs.id==id).first():
            return {f"File With Id={id} Not Found : All Data ":db.query(models.Songs).all()}
        AudioFiles= (db.query(models.Songs).filter(models.Songs.id==id).first() or db.query(models.Songs).all())
        return AudioFiles
    elif model_name == model_name.Podcast:
       if not db.query(models.Songs).filter(models.Podcast.id==id).first():
            return {f"File With Id={id} Not Found : All Data ":db.query(models.Podcast).all()}
       AudioFiles= (db.query(models.Podcast).filter(models.Podcast.id==id).first() or db.query(models.Podcast).all())
       return AudioFiles
    elif model_name == model_name.Audiobook:
        if not db.query(models.Songs).filter(models.Audiobook.id==id).first():
            return {f"File With Id={id} Not Found : All Data ":db.query(models.Audiobook).all()}
        AudioFiles= (db.query(models.Audiobook).filter(models.Audiobook.id==id).first() or db.query(models.Audiobook).all())
        return AudioFiles
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"File with id {id} not found !!")
    pass

def update_Song(db:Session,id,model_name: schemas.ModelName,request:schemas.Song):
    duration = schemas.common.Duration(item.Duration_in_number_of_seconds)
    uploaded_time = schemas.common.CurrentDate(item.Uploaded_time)
    if model_name == model_name.Song:
        AudioFiles= db.query(models.Songs).filter(models.Songs.id==id) 
        AudioFiles.update(Name_of_the_song=request.Name_of_the_song,Duration_in_number_of_seconds=duration,Uploaded_time=uploaded_time,typedata=types)
        return AudioFiles.first()
    if not AudioFiles.first():
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Song File with the id {id} is not available")
    db.commit()
    pass

def update_Audiobook( db:Session,id,model_name: schemas.ModelName,request:schemas.Audiobook): 
    duration = schemas.common.Duration(item.Duration_in_number_of_seconds)
    uploaded_time = schemas.common.CurrentDate(item.Uploaded_time)
    if model_name == model_name.Audiobook:
        AudioFiles= db.query(models.Audiobook).filter(models.Audiobook.id==id)
        AudioFiles.update(Title_of_the_audiobook=request.Title_of_the_audiobook,Author_of_the_title=request.Author_of_the_title,Narretor=request.Narretor,Duration_in_number_of_seconds=duration,Uploaded_time=uploaded_time)
        return AudioFiles.first()
    if not AudioFiles.first():
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Audiobook File with the id {id} is not available")
    db.commit()
    pass

def update_Podcast( db:Session,id,model_name: schemas.ModelName,request:schemas.Podcast): 
    duration = schemas.common.Duration(item.Duration_in_number_of_seconds)
    uploaded_time = schemas.common.CurrentDate(item.Uploaded_time)
    if model_name == model_name.Podcast:
        AudioFiles= db.query(models.Podcast).filter(models.Podcast.id==id)
        AudioFiles.update(Name_of_the_podcast=request.Name_of_the_podcast,Duration_in_number_of_seconds=duration,Uploaded_time=uploaded_time,Participants=request.Participants,Host=request.Host)
        return AudioFiles.first()
    if not AudioFiles.first():
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"Podcast File with the id {id} is not available")
    db.commit()
    pass

def delete_data(db:Session,id,model_name: schemas.ModelName):
    if model_name == model_name.Song:
        AudioFiles= db.query(models.Songs).filter(models.Songs.id==id)
        if not AudioFiles.first():
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"File with the id {id} is not available")
        AudioFiles.delete(synchronize_session=False)
        db.commit()
    if model_name == model_name.Podcast:
        AudioFiles= db.query(models.Podcast).filter(models.Podcast.id==id)
        if not AudioFiles.first():
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"File with the id {id} is not available")
        AudioFiles.delete(synchronize_session=False)
        db.commit()
    if model_name == model_name.Audiobook:
        AudioFiles= db.query(models.Audiobook).filter(models.Audiobook.id==id)
        if not AudioFiles.first():
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=f"File with the id {id} is not available")    
        AudioFiles.delete(synchronize_session=False)
        db.commit()
    if not AudioFiles.first():
        raise HTTPException( detail=f"File with the id {id} is Successfully Deleted")
    pass