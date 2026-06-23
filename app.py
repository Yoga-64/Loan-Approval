import pandas as pd
import pickles
from pydantic import BaseModel  ,Field
from typing import Annotated,Literal
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI
import streamlit as st
app=FastAPI()
@app.get("/about")
def about():
    return {"Message":"This is a Loan-Prediction Api model"}
def load_model():
    with open("loan_model.pkl","rb") as f:
        model=pickle.load(f)
    return model
class Loan(BaseModel):
    no_of_dependents:Annotated[int,Field(...,description="No of dependents")]
    education:Literal["Graduate","Not Graduate"]
    self_employed:Literal["Yes","No"]
    income_annum:Annotated[int,Field(...,description="Income of the borrower")]
    loan_amount:Annotated[int,Field(...,description="Loan amount of the borrower")]
    loan_term:Annotated[int,Field(...,description="Loan amount by the borrower")]
    cibil_score:Annotated[int,Field(...,description="Cibil score of the borrower")]
    residential_assets_value:Annotated[int,Field(...,description="Residential property value of the borrower")]
@app.post("/predict")
def loan_prediction(loan:Loan):
    model =load_model()
    input_data=loan.model_dump()
    input_df=pd.DataFrame([input_data])
    prediction=model.predict(input_df)
    return {
    "message": f"The prediction is {prediction[0]}"
}