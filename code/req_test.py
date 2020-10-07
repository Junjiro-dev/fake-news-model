import requests

data = {"title": "Fuentes cercanas al presidente reportan apocalipsis."}
response = requests.post("{}/".format("http://127.0.0.1:5000"), json =data )
print("Predicción: ")
print(response.json())