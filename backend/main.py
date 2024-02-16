from typing import Union
from fastapi import FastAPI
from dbTools import dbTools

app = FastAPI()

@app.get("/score-from-user/{score}")
def read_item(score: int):
    dbTools.add_score(score)
    return {"score-from-user": score}


@app.get("/statistics/")
def get_statistics():
    result = dbTools.get_statistics()
    return {
        "statistics": result
    }