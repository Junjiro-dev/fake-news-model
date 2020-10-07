from flask import Flask,jsonify,request
from processing.data_management import load_pipeline
import joblib
import pickle
import os
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
        return  jsonify({"about":"Hello World"})

if __name__ == '__main__':
    app.run(debug=True)