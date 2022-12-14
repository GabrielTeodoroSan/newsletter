import sqlite3
import datetime


def insert(notice):
    con = getConnection()
    cur = con.cursor()

    try:
        executeInserction(con, cur, notice)
        print("Dados inseridos com sucesso...")
    except:
        print("Ocorreu um erro ao inserir os dados...")

    con.close()


def getConnection():
    return sqlite3.connect('../database.db')


def executeInserction(con, cur, notice):
    sql_command = """INSERT INTO notices(title, url, image, created_in) VALUES(?, ?, ?, ?)"""
    cur.execute(sql_command, (notice[0], notice[1], notice[2], datetime.datetime.now()))
    con.commit()