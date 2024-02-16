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


def get_statistics() -> dict:
    connection = sqlite3.connect("scores.db")

    cursor = connection.cursor()

    cursor.execute("select count(*) from Score where score_value = 5")

    count_5 = cursor.fetchone()

    cursor.execute("select count(*) from Score where score_value = 4")

    count_4 = cursor.fetchone()

    cursor.execute("select count(*) from Score where score_value = 3")

    count_3 = cursor.fetchone()

    cursor.execute("select count(*) from Score where score_value = 2")

    count_2 = cursor.fetchone()

    cursor.execute("select count(*) from Score where score_value = 1")

    count_1 = cursor.fetchone()

    connection.close()

    return {
        "count_5": count_5,
        "count_4": count_4,
        "count_3": count_3,
        "count_2": count_2,
        "count_1": count_1
    }

