from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)
model = pickle.load(open("D:\\EDA\\Diabetes_Predictor v1.0\\Diabetes_Predictor.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        gender = request.form['gender']
        if gender == 'Female':
            gender = 1
        elif gender == 'Male':
            gender = 2
        else:
            gender = 3
            
        age = float(request.form['age'])
        
        hypertension = request.form['hypertension']
        if hypertension == 'Present':
            hypertension = 1
        else:
            hypertension = 0
            
        heart_disease = request.form['heart_disease']
        if heart_disease == 'Present':
            heart_disease = 1
        else:
            heart_disease = 0
            
        smoking_history = request.form['smoking_history']
        if smoking_history == 'Never':
            smoking_history = 1
        elif smoking_history == 'No Information':
            smoking_history = 2
        elif smoking_history == 'Current':
            smoking_history = 3
        elif smoking_history == 'Former':
            smoking_history = 4
        elif smoking_history == 'Ever':
            smoking_history = 5
        else:
            smoking_history = 6
            
        bmi = float(request.form['bmi'])
        HbA1c_level = float(request.form['HbA1c_level'])
        blood_glucose_level = float(request.form['blood_glucose_level'])
        
        prediction = model.predict([[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]])
        output = prediction[0]
        
        if output == 1:
            result = "The patient is likely to have diabetes."
        else:
            result = "The patient is not likely to have diabetes."

        return render_template('WebApp.html', prediction_text=result)

    return render_template("WebApp.html")


if __name__ == "__main__":
    app.run(debug=True)