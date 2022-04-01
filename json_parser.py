import requests
import json
from requests.exceptions import HTTPError

dishes = {
    "Strawberry ice cream": 1,
    "Pancakes": 2,
    "Waffles": 3,
    "Fish": 4
}


class ResponseError(Exception):
    pass


def get_recepie(dish):
    if dish not in dishes:
        raise KeyError(f"No such dish in dictionary: {dish}")
    url = 'https://granny-crud.herokuapp.com/apis/getrecommendations/' + \
        str(dishes[dish])
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTPError
        json_data = response.json()
        print("Json response:")
        print(json_data)
        return json_data
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
        raise HTTPError
    except Exception as error:
        print(f'Other error occurred: {error}')
        raise ResponseError


def save_data(*json_data):
    with open('json_data.json', 'w') as file:
        data = []
        for recepie in json_data:
            data.append(recepie[0])
        json.dump(data, file, indent=4)


def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False


def main():
    data1 = get_recepie("Strawberry ice cream")
    data2 = get_recepie("Pancakes")
    data3 = get_recepie("Fish")
    save_data(data1, data2, data3)


if __name__ == "__main__":
    main()
