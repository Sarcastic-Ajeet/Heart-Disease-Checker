from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd

application=Flask(__name__)
app=application

predictor=pickle.load(open("model\modelprediction.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predicted",methods=["GET","POST"])
def predict_data():
    if request.method=="POST":
        male=int(request.form.get('male'))
        age = int(request.form.get('age'))
        education = float(request.form.get('education'))
        currentSmoker = int(request.form.get('currentSmoker'))
        cigsPerDay = float(request.form.get('cigsPerDay'))
        BPMeds = float(request.form.get('BPMeds'))
        prevalentStroke = int(request.form.get('prevalentStroke'))
        prevalentHyp = int(request.form.get('prevalentHyp'))
        diabetes = int(request.form.get('diabetes'))
        totChol = float(request.form.get('totChol'))
        sysBP = float(request.form.get('sysBP'))
        diaBP = float(request.form.get('diaBP'))
        BMI = float(request.form.get('BMI'))
        heartRate = float(request.form.get('heartRate'))
        glucose = float(request.form.get('glucose'))


        result=predictor.predict([[male,age,education,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
        return render_template("home.html",results=result)
    else:
        return render_template("home.html")
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
        