from fastapi import Body,FastAPI, Depends, status, HTTPException,Query,Path
from uuid import UUID

from datetime import datetime, time, timedelta
from typing import Optional
from typing import List,Union,Any,Dict
from pydantic import BaseModel
from AudioServer import schemas, models,crud
from .database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .Routers import audiofile
import uvicorn
# Launch API SERVER
app = FastAPI()
# Create DB Engine
models.Base.metadata.create_all(engine)

app.include_router(audiofile.router)


# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9900)