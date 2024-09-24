import requests

API_KEY = "a2348c14a2c0963b262528feb379ffd8"

def get_data(place, forecast_days):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values =  8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__" :
    print(get_data(place="Catania", forecast_days=3))