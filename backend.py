import requests

API_KEY = "e843309fdd20fd92ae1b671a6623d810"


def get_data(place, forecast_days=0):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8 * forecast_days
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__ == "__main__":
    filtered_data = get_data(place="Tokyo", forecast_days=1)
    print([dict_["dt_txt"] for dict_ in filtered_data])