import pandas as pd
import joblib

def load_dataset():
    data = pd.read_csv("fake_news_classifier\code\datasets\cleaned_train_test_dataset.csv", index_col=0)
    return data

def save_pipeline(pipeline_to_save):
    save_path = "fake_news_classifier\code/trained_models/fake_news_model.pkl"
    joblib.dump(pipeline_to_save, save_path)
    print("Saved Pipeline")


def load_pipeline():
    save_path = "fake_news_classifier\code/trained_models/fake_news_model.pkl"
    trained_model = joblib.load(save_path)
    print("Pipeline loaded")
    return trained_model