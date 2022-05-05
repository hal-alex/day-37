import requests

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": "",
    "username": "alex111",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=parameters)
print(response.text)