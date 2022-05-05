import requests
from datetime import datetime

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

today_date = datetime(year=2022, month=5, day=2)

current_date = today_date.strftime("%Y%m%d")

point_config = {
    "date": current_date,
    "quantity": "2.6",
}

update_point_endpoint = f"{create_point_endpoint}/{current_date}"

modify_point_config = {
    "quantity": "2.5",
}

# response = requests.put(url=update_point_endpoint, headers=headers, json=modify_point_config)
#
# print(response.text)

response = requests.delete(url=update_point_endpoint, headers=headers)

print(response.text)