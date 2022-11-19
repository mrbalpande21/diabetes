from flask import Flask, render_template, jsonify, request
from Proj_Data.utils import Diabetes
# from Proj_Data import config_data


app = Flask(__name__)

@app.route("/")

def test():
    return render_template("index.html")


@app.route("/predict",methods=['POST'])

def test1():
    data = request.form

    Glucose      =eval(data["Glucose"])
    BloodPressure=eval(data["BloodPressure"])
    SkinThickness=eval(data["SkinThickness"])
    Insulin      =eval(data["Insulin"])
    BMI          =eval(data["BMI"])
    DiabetesPedigreeFunction=eval(data["DiabetesPedigreeFunction"])
    Age          =eval(data["Age"])

    obj = Diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = obj.predict_dia()

    return render_template("after.html", data=result)

if __name__ == "__main__":
    app.run()