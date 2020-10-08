import requests
from polyglot.downloader import downloader
from shutil import copyfile
from polyglot.text import Text
import os


print("copying file")
copyfile(str(os.getcwd())+"\\fake_news_classifier\\code\\es.sent.pkl.tar.bz2", str(downloader.default_download_dir()))
print("file copied? Testing existence")
text = Text("Este texto es de prueba").polarity
print(text)


data = {"title": "Fuentes cercanas al presidente reportan apocalipsis."}
#response = requests.get("{}/".format("https://felix-obando-tesis.uc.r.appspot.com"))
#response = requests.post("{}/".format("https://felix-obando-tesis.uc.r.appspot.com"), json =data )
print("Predicción: ")
#print(response.json())