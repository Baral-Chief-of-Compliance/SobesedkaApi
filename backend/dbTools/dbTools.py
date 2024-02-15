import sqlite3
from datetime import datetime


def add_score(score: int) -> None:
    connection = sqlite3.connect("scores.db")

    cursor = connection.cursor()

    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    cursor.execute('''insert into Score (score_value, score_date) values (?, ?)''', (score, now))

    connection.commit()

    connection.close()


def create_db() -> None:
    connection = sqlite3.connect("scores.db")

    cursor = connection.cursor()

    cursor.execute('''create table Score (score_id integer primary key AUTOINCREMENT, score_value integer, score_date text)''')

    connection.commit()

    connection.close()

