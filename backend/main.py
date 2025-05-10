from database import conn, encerra_conn
from fastapi import FastAPI
import uvicorn
from crud.insert import insert_obra
from crud.select import seleciona
from crud.update import autor_inp, lingua_inp, edicao_inp, anopubli_inp, npag_inp, title_inp
from crud.delete import delete 
from routes.obras import router as obra_router


app = FastAPI()
app.include_router(obra_router)

connection = conn()


# products = [
#     {
#         "id": 1,
#         "nome": "smartphone",
#         "descricao": "um telefone inteligente ",
#         "preco": 1999.99,
#         "disponivel": True
#     },
#     {
#         "id": 2,
#         "nome": "notebook",
#         "descricao": "um telefone maior ",
#         "preco": 3999.99,
#         "disponivel": False
#     }
# ]



@app.get("/produtos")
def listarobras():
    """Listar obras."""
    return seleciona()

encerra_conn(connection)
