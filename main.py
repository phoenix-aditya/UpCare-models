from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from starlette.responses import FileResponse,RedirectResponse
import json
import pickle
import sys

from model import *

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HeartDisease(BaseModel):
    age: int
    sex: int
    severity: int
    cholestrol: int
    bp: int
    heartrate: int

class ThyroidDisease(BaseModel):
    age: float
    sex: float
    On_thyroxine: float
    Query_on_thyroxine: float
    On_antithyroid_medication: float
    sick: float
    pregnant: float
    thyroidSurgery: float
    I131_treatment: float
    Query_hypothyroid: float
    Query_hyperthyroid: float
    Lithium: float
    Goiter: float
    Tumor: float
    Hypopituitary: float
    Psych: float
    TSH: float
    T3: float
    TT4: float
    T4U: float
    FTI: float

@app.get("/")
def index():
    return RedirectResponse(url='/docs')

@app.post("/heartDisease/")
def heartDisease(info: HeartDisease):
    data = [[
        info.age,
        info.sex,
        info.severity,
        info.cholestrol,
        info.bp,
        info.heartrate
    ]]
    res = predictHeartDisease(data)
    return res

@app.post("/thyroidDisease/")
def thyroidDisease(info: ThyroidDisease):
    data = [[
        info.age,
        info.sex,
        info.On_thyroxine,
        info.Query_on_thyroxine,
        info.On_antithyroid_medication,
        info.sick,
        info.pregnant,
        info.thyroidSurgery,
        info.I131_treatment,
        info.Query_hypothyroid,
        info.Query_hyperthyroid,
        info.Lithium,
        info.Goiter,
        info.Tumor,
        info.Hypopituitary,
        info.Psych,
        info.TSH,
        info.T3,
        info.TT4,
        info.T4U,
        info.FTI
    ]]
    print("here: ",data)
    res = predictThyroidDisease(data)
    return res
