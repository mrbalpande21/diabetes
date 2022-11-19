import numpy as np
import pickle
import json
# import config_data

import os

model_file = os.path.join("Proj_Data","KNN_Dia_model.pkl")

normal_file = os.path.join("Proj_Data","normalization.pkl")

json_file = os.path.join("Proj_Data","dia_col_data.json")

class Diabetes():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose      =Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin      =Insulin
        self.BMI          =BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age          =Age


    def load_files(self):

        with open(model_file, "rb") as f:
            self.model = pickle.load(f)

        with open(normal_file, "rb") as n:
            self.normal = pickle.load(n)

        with open(json_file, "r") as j:
            self.json_file = json.load(j)

    def predict_dia(self):
        self.load_files()

        test_array = np.zeros(len(self.json_file["columns"]))

        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age

        normal_val = self.normal.transform([test_array])
        prediction = self.model.predict(normal_val)[0]

        return prediction


