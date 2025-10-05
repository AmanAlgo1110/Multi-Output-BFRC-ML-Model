import joblib
import streamlit as slt
import numpy as np
import pandas as pd
loaded_model=joblib.load("model_multioutout.pkl")
slt.title("BFRC")
slt.write("Enter input values below:")
feature2=slt.number_input("Feature-2",min_value=0.0,value=0.0)
feature1=slt.number_input("Feature-1",min_value=0.0,value=0.0)
feature3=slt.number_input("Feature-3",min_value=0.0,value=0.0)
feature4=slt.number_input("Feature-4",min_value=0.0,value=0.0)
feature5=slt.number_input("Feature-5",min_value=0.0,value=0.0)
feature6=slt.number_input("Feature-6",min_value=0.0,value=0.0)
feature7=slt.number_input("Feature-7",min_value=0.0,value=0.0)
feature8=slt.number_input("Feature-8",min_value=0.0,value=0.0)
x_input=pd.DataFrame({
    'Water-cement ratio':[feature1],
    'Fly ash kg/m³':[feature2],
    'Crude aggregate kg/m³':[feature3],
    'Fine aggregate kg/m³':[feature4],
    'Silica ash kg/m³':[feature5],
    'Fiber diameter-mm':[feature6],
    'Fiber length-mm':[feature7],
    'Fiber content-%':[feature8]
})
for i in x_input.columns:
    x_input[i]=np.log1p(x_input[i])
if slt.button("predict"):
    y_pred=loaded_model.predict(x_input)
    y_pred=np.expm1(y_pred)
    slt.success(f"Compressive strength is : {y_pred[0][0]} Mpa")
    slt.success(f"Flexural strength is : {y_pred[0][1]} Mpa")