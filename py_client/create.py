import requests


endpoint= "http://localhost:8000/api/products/"

data = {
    'title': "this field is done",
    'price': 3000
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
