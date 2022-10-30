import joblib
import numpy as np
import pandas as pd
import json

def predictHeartDisease(data):
    loaded_rf = joblib.load("models/heartDiseasePredictor.joblib")
    predicted = loaded_rf.predict(data)
    return {'status':'OK','response':predicted[0]}

def predictThyroidDisease(data):
    loaded_scaler = joblib.load("models/thyroidScaler.joblib")
    loaded_rf = joblib.load("models/thyroidDiseaseModel.joblib")

    scaled_sample = loaded_scaler.transform(data)
    print("scaled sample: ", scaled_sample)
    predict = loaded_rf.predict(scaled_sample)
    return {'status':'OK','response':predict.tolist()[0]}


def norm(x):
    res = [[
        x[0][0]-635589406.6549913/646655758.3289639,
        x[0][1]-42.25797846733888/0.2907192152409467,
        x[0][2]-71.36106653596275/0.6214539427248971
    ]]
    return res


def predictAllergy(data):
    allergy_codes = ['3718001',
                    '84489001',
                    '102263004',
                    '111088007',
                    '256277009',
                    '256355007',
                    '260147004',
                    '264287008',
                    '288328004',
                    '412071004',
                    '735029006',
                    '735971005',
                    '762952008',
                    '782576004',
                    '442571000124108']
    
    loaded_rf = joblib.load("models/geolocationAllergyPrediction.joblib")

    scaled_sample = norm(data)
    res = loaded_rf.predict(scaled_sample)

    predicted = np.array(res[0]).argsort()[-5:]
    allergy_ids = [allergy_codes[i] for i in predicted]
    allergy_details = pd.read_csv('data/AllergiesList.csv',index_col='CODE',dtype={'CODE':'string'})
    allergy_details = allergy_details.fillna('')
    res = []
    for code in allergy_ids:
        res.append(allergy_details.loc[code].to_dict())
    
    return {'status':'OK','response':res}


