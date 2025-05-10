from database import conn, encerra_conn

connection = conn()
cursor = connection.cursor()

def atualiza_autor(autor_novo, ID_obra):
    cmd_update = f"UPDATE obras SET autor='{autor_novo}' WHERE ID_obra={ID_obra}"
    cursor.execute(cmd_update)
    connection.commit()
    print("autor atualizado com sucesso")

def autor_inp():
    autor = input("qual o novo autor? \n")
    id = int(input("Qual o ID da obra? \n"))

    return atualiza_autor(autor, id)


def atualiza_titulo(titulo_novo, ID_obra):
    cmd_update = f"UPDATE obras SET titulo='{titulo_novo}' WHERE ID_obra={ID_obra}"
    cursor.execute(cmd_update)
    connection.commit()
    print("titulo atualizado com sucesso")

def title_inp():
    titulo = input("qual o novo titulo? \n")
    id = int(input("Qual o ID da obra? \n"))

    return atualiza_titulo(titulo, id)


def atualiza_anopubli(anopubli_nova, ID_obra):
    cmd_update = f"UPDATE obras SET ano_public='{anopubli_nova}' WHERE ID_obra={ID_obra}"
    cursor.execute(cmd_update)
    connection.commit()
    print("ano de publicação atualizado com sucesso")

def anopubli_inp():
    ano = input("qual o novo ano de publicação? \n")
    id = int(input("Qual o ID da obra? \n"))

    return atualiza_anopubli(ano, id)


def atualiza_edicao(edicao_nova, ID_obra):
    cmd_update = f"UPDATE obras SET edicao='{edicao_nova}' WHERE ID_obra={ID_obra}"
    cursor.execute(cmd_update)
    connection.commit()
    print("edicao atualizada com sucesso")

def edicao_inp():
    edicao = input("qual a nova edição? \n")
    id = int(input("Qual o ID da obra? \n"))

    return atualiza_edicao(edicao, id)

    
def atualiza_num_paginas(npag_novo, ID_obra):
    cmd_update = f"UPDATE obras SET num_paginas='{npag_novo}' WHERE ID_obra={ID_obra}"
    cursor.execute(cmd_update)
    connection.commit()
    print("número de páginas atualizado com sucesso")

def npag_inp():
    npag = input("qual o novo número de páginas? \n")
    id = int(input("Qual o ID da obra? \n"))

    return atualiza_num_paginas(npag, id)


def atualiza_lingua(lingua_nova, ID_obra):
    cmd_update = f"UPDATE obras SET lingua='{lingua_nova}' WHERE ID_obra={ID_obra}"
    cursor.execute(cmd_update)
    connection.commit()
    print("lingua atualizada com sucesso")

def lingua_inp():
    lingua = input("qual a nova lingua? \n")
    id = int(input("Qual o ID da obra? \n"))

    return atualiza_lingua(lingua, id)

