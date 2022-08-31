import requests


endpoint= "http://localhost:8000/api/products/"

data = {
    'title': "I jsut added this",
    'price': 3000
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
