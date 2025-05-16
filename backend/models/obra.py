from pydantic import BaseModel
from typing import Optional
from datetime import date

class ObraBase(BaseModel):
    titulo: str
    edicao: Optional[str]   # Opcional
    ano_publicacao: date
    autor: str
    num_paginas: Optional[int] 
    status: Optional[str] 
class ObraCreate(ObraBase):
    pass

class ObraResponse(ObraBase):
    ID_obra: int

    class Config:
        from_attributes = True #conversão de ORM's/dicts