import numpy as np
import pandas as pd 
from polyglot.text import Text
from polyglot.downloader import downloader as pl_download


from processing.data_management import load_pipeline

fake_news_trained_pipeline = load_pipeline()

def make_prediction(news_title):

    prediction = fake_news_trained_pipeline.predict([news_title])
    print(prediction)
    results = {
        'prediction': prediction,
    }

    return results
def make_test_prediction():
    text_title="Fuentes cercanas al presidente reportan apocalipsis"
    prediction = fake_news_trained_pipeline.predict([text_title])
    print(prediction)
    results = {
        'prediction': prediction,
    }
    return results
#Uncomment for testing
if __name__=='__main__':
    make_test_prediction()