from database import conn, encerra_conn

connection = conn()
cursor = connection.cursor()

def deleta(ID_obra):
    cmd_delete = f"DELETE FROM obras WHERE ID_obra='{ID_obra}'"
    cursor.execute(cmd_delete)
    connection.commit()
    print("obra deletada com sucesso")

def delete():
    id = int(input("Qual o id a ser deletado?\n"))
    return deleta(id)