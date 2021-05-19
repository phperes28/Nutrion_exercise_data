import requests
from ex_data import API_KEY, APP_ID
from datetime import datetime


#----------------------------------------------------Nutri API------------------------------------------------------#
EX_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"


resposta = input("Tell me which exercises you did: ")

params = {
 "query": resposta,
 "gender":"male",
 "weight_kg":75,
 "height_cm":175,
 "age":31
}

HEADERS ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


ex_response = requests.post(url=EX_ENDPOINT, json=params, headers=HEADERS)
result = ex_response.json()
print(ex_response.text)
today = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%H:%M")



# #----------------------------------------------------Sheety API------------------------------------------------------#
SHEETY_ENDPOINT = "https://api.sheety.co/c6ca40e3930a12e07ef9c74d91a890ff/myWorkouts/página1"


for exercise in result["exercises"]:
    sheet_inputs = {
        "página1": {
            "date": today,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)
