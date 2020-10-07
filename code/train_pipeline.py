#Import Libraries
import pandas as pd
import numpy as np

#Import other files/modules
from processing.data_management import load_dataset, save_pipeline
import processing.transformer as tr
import pipeline


def run_training():
    """Train the model"""

    #Read Data
    data = load_dataset()
    #Training pipeline
    pipeline.fake_news_pipeline.fit(data["traducción"].values, data["fake"].values)
    save_pipeline(pipeline_to_save=pipeline.fake_news_pipeline)

if __name__=='__main__':
    run_training()
    print("pipeline trained")