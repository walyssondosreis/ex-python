# coding: utf-8
# TITLE: CONEXÃO PYTHON COM POSGRESQL
# AUTHOR: WALYSSON DOS REIS

import psycopg2

con = psycopg2.connect(host='localhost',port='5433',user='postgres',password='123',dbname='walldb')# conecta no banco de Dados
c = con.cursor() # armazena o cursor do banco que nada mais faz do que apontar para uma tupla/linha
c.execute("INSERT INTO teste (nome) VALUES ('NOME10')") # grava no banco
#con.commit() # Efetiva de fato a alteração/ inserção no banco
#con.rollback() # Anula a inserção no banco , bloco BEGIN no SQL

k=input('Deseja Inserir? ')
if k.upper()=='S':
    con.commit()
    con.close() # encerra a conexão
else:
    con.rollback() #
    con.close() # encerra a conexao

# PSYCOPG2
#http://initd.org/psycopg/download/

# TUTORIAL DE CONEXÂO PYTHON POSTGRESQL
# http://www.programeempython.com.br/blog/bancos-de-dados-com-python-postgresql/
# http://www.devmedia.com.br/como-criar-uma-conexao-em-postgresql-com-python/34079

