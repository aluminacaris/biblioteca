from database import conn, encerra_conn

connection = conn()
cursor = connection.cursor()

def seleciona():
    cmd_select = "SELECT ID_obra, titulo, ano_public, edicao, num_paginas, lingua, autor FROM obras;"
    cursor.execute(cmd_select)
    acoes = cursor.fetchall()
    return acoes
