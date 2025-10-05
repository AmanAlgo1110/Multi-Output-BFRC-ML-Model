import joblib
import streamlit as slt
import numpy as np
import pandas as pd
loaded_model=joblib.load("model_multioutout.pkl")
slt.title("BFRC")
slt.write("Enter input values below:")
feature1=slt.number_input("Water-cement ratio",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature2=slt.number_input("Fly ash kg/m³",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature3=slt.number_input("Crude aggregate kg/m³",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature4=slt.number_input("Fine aggregate kg/m³",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature5=slt.number_input("Silica ash kg/m³",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature6=slt.number_input("Fiber diameter-mm",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature7=slt.number_input("Fiber length-mm",min_value=0.0,value=0.00,step=.0001,format="%.4f")
feature8=slt.number_input("Fiber content-%",min_value=0.0,value=0.00,step=.0001,format="%.4f")
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



