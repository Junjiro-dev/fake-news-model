from flask import Flask,jsonify,request
from processing.data_management import load_pipeline
import joblib
import pickle

from polyglot.downloader import downloader
from shutil import copyfile
from polyglot.text import Text


app = Flask(__name__)

fake_news_trained_pipeline = load_pipeline()

@app.route("/", methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        data = request.get_json()
        print(data)
        title = str(data["title"])
        prediction = "falsa" if bool(fake_news_trained_pipeline.predict([title])[0]) else "confiable"
        print("pred: "+ prediction)
        ans = jsonify({"pred": prediction})
        print(ans)
        return ans
    else:
        print("copying file")
        copyfile(str(os.getcwd())+"\\fake_news_classifier\\code\\es.sent.pkl.tar.bz2", str(downloader.default_download_dir()))
        print("file copied? Testing existence")
        text = Text("Este texto es de prueba").polarity
        print(text)
        return  jsonify({"about":"Hello World"})

if __name__ == '__main__':
    app.run(debug=True)