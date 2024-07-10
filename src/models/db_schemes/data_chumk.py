from pydantic import BaseModel , Filed , validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    
    _id : Optional[ObjectId]
    chunk_text: str = Filed(... , min_length = 1)
    chunk_metadate: dict
    chunk_order:int = Filed(... , gt=0)
    chunk_project_id: object
    
    
    class Config:
        arbitrary_types_allowed = True