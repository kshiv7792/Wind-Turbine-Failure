import numpy as np

import pickle
# from sklearn.externals import joblib       

#import xgboost as xgb
import pandas as pd
from flask import Flask, request, render_template
# import joblib


app = Flask(__name__)
model = pickle.load(open('model_final.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) 
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['Wind_speed', 'Power', 'Nacelle_ambient_temperature', 'Generator_bearing_temperature',
       'Gear_oil_temperature', 'Ambient_temperature', 'Rotor_Speed',
       'Nacelle_temperature', 'Generator_speed', 'Yaw_angle', 'Wind_direction',
       'Gear_box_inlet_temperature', 'Bearing_temperature',
       'Wheel_hub_temperature']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
        
    return render_template('index.html',prediction_text=output)

if __name__ == "__main__":
#     app.debug = True
    app.run()