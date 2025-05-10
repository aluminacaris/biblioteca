from pydantic import BaseModel
from typing import Optional

class ObraBase(BaseModel):
    titulo: str
    edicao: Optional[str] = None  # Opcional
    ano_publicacao: Optional[int] = None
    autor: str
    num_paginas: Optional[int] = None
    status: Optional[str] = None
class ObraCreate(ObraBase):
    pass

class ObraResponse(ObraBase):
    ID_obra: int

    class Config:
        from_attributes = True #conversão de ORM's/dicts