import joblib

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
