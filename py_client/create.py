import requests

headers = {"Authorization": "Token 40ba287261f6dff3e4c3c0074d8c9b9e94735c97" }
endpoint= "http://localhost:8000/api/products/"

data = {
    'title': "I jsut added this",
    'price': 3000
}

get_response = requests.post(endpoint, json=data, headers= headers)

print(get_response.json())
