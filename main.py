import sqlite3
from openpyxl import Workbook, load_workbook
import pandas as pd

connection = sqlite3.connect('filmes.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS filme(
    data TEXT NOT NULL, 
    nota int,
    nome TEXT NOT NULL
);
''')


def menu():
    print('*******************************')
    print('* i - Inserir novo filme      *')
    print('* l - Listar Filmes           * ')
    print('* e - Ver detalhes            * ')
    print('* s - Sair                    *')
    print('*******************************')


def get_movies(nome):
    cursor.execute(f'''
        SELECT data, nota FROM filme
        WHERE nome = '{nome}'
''')



    if cursor.rowcount == 0:
        print('Filme não cadastrado! Use l para verificar.')
    else:
        for filmes in cursor.fetchall():
            print(filmes)


def insert_movie(nome, data, nota):
    cursor.execute(f'''
        INSERT INTO filme (nome, data, nota)
        VALUES ('{nome}', '{data}', '{nota}')
    ''')
    connection.commit()


def show_movies():
    cursor.execute('''
    SELECT nome FROM filme;
    ''')
    for nome in cursor.fetchall():
        print(nome)


while True:
    menu()
    option = input('O que deseja fazer agora? ').lower()
    if option not in ['l', 'i', 'e', 's']:
        print('Opção inválida')
        continue

    if option == 's':
        break

    if option == 'i':
        nome = input('Qual o nome do filme?')
        data = input('Em que data foi assistido? ')
        nota = input('Qual a sua nota para o filme? ')
        insert_movie(nome, data, nota)

    if option == 'l':
        show_movies()

    if option == 'e':
        filmes = input('Qual filme você deseja ver mais detalhes? ')
        get_movies(filmes)
connection.close()
