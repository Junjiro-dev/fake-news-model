import requests
from polyglot.downloader import downloader
from shutil import copyfile
from polyglot.text import Text

#Used for testing

data = {"title": "Fuentes cercanas al presidente reportan apocalipsis."}
#response = requests.get("{}/".format("https://felix-obando-tesis.uc.r.appspot.com"))
response = requests.post("{}/".format("http://127.0.0.1:5000"), json =data )
print("Predicción: ")
print(response.json())