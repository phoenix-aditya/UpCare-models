# WeCARE APIS


## Deployed API'S

https://wecare-model.herokuapp.com/

---

---

# Heart Disease Prediction Model

## Input

1. age (integer)
2. sex (0-female, 1-male)
3. severity of chest pain (integer between 1-4)
4. cholestrol (125-565)
5. blood pressure (systolic) (95-200)
6. heart rate (70-200)

```python
x_test = [[ 63,   1,   1, 145, 233, 150]]
```

## Output

string denoting Presense or Absence of Heart Diseases

```python
['Presence'] or ['Absence']
```

## Model calling

```python
import joblib

loaded_rf = joblib.load("models/heartDiseasePredictor.joblib")
predicted = loaded_rf.predict(x_test)
# predicted contains list of strings denoting predictions
```

## API calling

### Address

```python
/heartDisease/
```

### Request Body

```python
{
  "age": 63,
  "sex": 1,
  "severity": 1,
  "cholestrol": 145,
  "bp": 233,
  "heartrate": 150
}
```

### Response

```python
{
  "status": "OK",
  "response": "Presence"
}
```

---

# Thyroid Disease Prediction Model

## Input

0 for false, 1 for true

1. Age
2. Sex (0-female, 1-male)
3. On_thyroxine (0 for false, 1 for true)
4. Query_on_thyroxine (0 for false, 1 for true)
5. On_antithyroid_medication (0 for false, 1 for true)
6. Sick (0 for false, 1 for true)
7. Pregnant (0 for false, 1 for true)
8. Thyroid surgery (0 for false, 1 for true)
9. I131_treatment (0 for false, 1 for true)
10. Query_hypothyroid (0 for false, 1 for true)
11. Query_hyperthyroid (0 for false, 1 for true)
12. Lithium
13. Goiter
14. Tumor
15. Hypopituitary
16. Psych
17. TSH
18. T3
19. TT4
20. T4U
21. FTI

```python
sample = [[-1.4823020657324806,
 -0.6615038757794697,
 -0.38732927269920464,
 -0.1251498325938894,
 -0.113784030146875,
 -0.1996819198449703,
 -0.10466640425549774,
 -0.11929528643516245,
 -0.13020730314182272,
 -0.26490647141300877,
 -0.2717490219969306,
 -0.11315598734894247,
 -0.0909090909090909,
 -0.16196681076731126,
 -0.01178756901918138,
 -0.22675291789239235,
 -0.20068131643515402,
 1.329595656848054,
 0.933299250487629,
 1.8429121666107076,
 -0.14444759182149772]]
```

## Output

Category of the thyroid predicted

array containing category value

```python
array([3])
```

## Model calling

```python
import joblib

loaded_scaler = joblib.load("models/thyroidScaler.joblib")
loaded_rf = joblib.load("models/thyroidDiseaseModel.joblib")

scaled_sample = loaded_scaler.transform(sample)
predict = loaded_rf.predict(scaled_sample)
```

## API calling

### Address

```python
/thyroidDisease/
```

### Request Body

```python
{
  "age": 0.24000,
  "sex": 0,
  "On_thyroxine": 0,
  "Query_on_thyroxine": 0,
  "On_antithyroid_medication": 0,
  "sick": 0,
  "pregnant": 0,
  "thyroidSurgery": 0,
  "I131_treatment": 0,
  "Query_hypothyroid": 0,
  "Query_hyperthyroid": 0,
  "Lithium": 0,
  "Goiter": 0,
  "Tumor": 0,
  "Hypopituitary": 0,
  "Psych": 0,
  "TSH": 0.00025,
  "T3": 0.03000,
  "TT4": 0.14300,
  "T4U": 0.13300,
  "FTI": 0.10800
}
```

### Response

```python
{
  "status": "OK",
  "response": 3
}
```

response denotes the category of the thyroid

---

# GeoLocation Allergy Prediction Model

## Input

1. age (float)
2. latitude (float)
3. longitude (float)

```python
x_test = [[ [789091200.0, 42.64548037467002, -71.39734343342467]]]
```

## Output

model returns probabilities of allergies corresponding to AllergyLabels variable

```python
array([[0.0999913 , 0.10006935, 0.10009937, ..., 0.10001634, 0.10002487,
        0.09999817]])
```

The details for every label is denoted in AllergyList csv

## Model calling

```python
import joblib

def norm2(x):
		# function has the mean of the value divided by respective std
    res = [[
        x[0][0]-635589406.6549913/646655758.3289639,
        x[0][1]-42.25797846733888/0.2907192152409467,
        x[0][2]-71.36106653596275/0.6214539427248971
    ]]
    return res

loaded_rf = joblib.load("../models/geolocationAllergyPrediction.joblib")
data = [[-2.1905921170725358, 0.08366228852026761, -0.144925575613581]]
scaled_data = norm2(data)

predicted = loaded_rf.predict(scaled_data)
# predicted contains output denoted above
```

## API calling

### Address

```python
/Allergy/
```

### Request Body

```python
{
  "age": 7.890912,
  "latitude": 4.264548,
  "longitude": -7.139734
}
```

### Response

```json
{
  "status": "OK",
  "response": [
    {
      "DESCRIPTION": "Wheat (substance)",
      "CATEGORY": "food",
      "REACTION1": "",
      "DESCRIPTION1": "",
      "SEVERITY1": "",
      "REACTION2": "",
      "DESCRIPTION2": "",
      "SEVERITY2": ""
    }
	]
}
```

Returns a list of dictionary as response of the API call containing details regarding 5 most probably allergies

---
