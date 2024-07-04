import requests
from datetime import datetime
USERNAME = "aryan483"
TOKEN ="ahbaskasashahah"
GRAPH_ID= "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "ahbaskasashahah",
    "username": "aryan483",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "kuro",    
}

headers = {
    "X-USER-TOKEN": TOKEN
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2024,month=7,day=3)
today = datetime.now()
pixela_data ={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many hrs do i code?"),
}

response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
print(response.text)
 
 
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixela_data ={
    "quantity":"15.9",
}


# response = requests.put(url=update_endpoint,json=new_pixela_data, headers=headers)
# print(response.text)


