import requests

TOKEN = ""
USERNAME = "alex111"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "miles",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

create_point_endpoint = f"{graph_endpoint}/{graph_config['id']}"

point_config = {
    "date": "20220504",
    "quantity": "2.7",
}

response = requests.post(url=create_point_endpoint, headers=headers, json=point_config)

print(response.text)