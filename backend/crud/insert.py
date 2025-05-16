from database import conn, encerra_conn
from datetime import datetime
from models.obra import ObraCreate

    # CREATE
def insert_obra(obra: ObraCreate):
    conn = None
    cursor = None

    try:
        connection = conn()
        cursor = connection.cursor()

        if isinstance(obra.ano_publicacao, str):
            # Assumindo o formato YYYY-MM-DD
            ano_publicacao = datetime.strptime(obra.ano_publicacao, '%Y-%m-%d').date()
        else:
            ano_publicacao = obra.ano_publicacao    

        cmd_insert = """INSERT INTO obras(titulo, edicao, ano_publicacao, autor, num_paginas, status) VALUES (%s,%s,%s,%s,%s,%s)
        RETURNING *; 
        """

        values = (
            obra.titulo,
            obra.edicao,
            obra.ano_publicacao,
            obra.autor,
            obra.num_paginas,
            obra.status
        )    

        cursor.execute(cmd_insert, values)
        new_obra = cursor.fetchone() 
        conn.commit()
        return new_obra
    
    except Exception as e:
        if conn:
            conn.rollback()
        raise Exception(f"erro fatal ao inserir obra: {str(e)}")        
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
  



