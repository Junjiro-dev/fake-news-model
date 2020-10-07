import requests

data = {"title": "Fuentes cercanas al presidente reportan apocalipsis."}
response = requests.post("{}/".format("https://felix-obando-tesis.uc.r.appspot.com/"), json =data )
print("Predicción: ")
print(response.json())