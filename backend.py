import requests

API_KEY = "YOU_API_KEY_GOES_HERE"


def get_data(city, days):
    """ Takes place by name, and days (1-5) returns JSON data with 3hr intervals """
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={days * 8}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    return filtered_data


if __name__ == "__main__":
    print(get_data(city="London", days=1))
