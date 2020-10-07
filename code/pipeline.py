from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

import processing.transformer as tr

fake_news_pipeline = Pipeline(
  [
    ('vectorization', tr.WordVectorizerPipeline()),
    ('classification', LinearSVC(dual=False))      
  ]
)

if __name__=='__main__':
  print("pipeline main")
else:
  print("importing pipeline.py as aux")