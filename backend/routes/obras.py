from fastapi import APIRouter, HTTPException
from crud.insert import insert_obra
from models.obra import ObraCreate, ObraResponse

router = APIRouter(prefix="/obras") #cria um roteador com prefixo obras, todo caminho daqui começa  com isso

@router.post("/", response_model=ObraResponse) #  esoecfica o formato da resposta pela validacao do pydantic
def criar_obra(obra: ObraCreate):
    try:
        obra_inserida = insert_obra(obra) #chama a func de criar obra, q é validaad pelo ObraCreate!!!! pleo pydantic
        return obra_inserida
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"erro fatal ao inserir obra: {str(e)}"
        ) 
