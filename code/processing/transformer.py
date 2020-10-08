import math
import spacy
import numpy
from polyglot.text import Text
from sklearn.base import BaseEstimator, TransformerMixin
from shutil import copyfile
import os
from polyglot.downloader import downloader



def round_prox(number):
    #round_prox rounds the number to the closest three decimal place
    return math.floor(number*1000 + 0.5)/1000

def singleSampleProcessPipeline(sampleText, spacy_model_instance):
    title = sampleText
    
    #We only use NER and POS pipelines
    doc = spacy_model_instance(title, disable=['parser'])
    
    #We count the pos attributes
    count_raw_POS = doc.count_by(spacy.attrs.POS)
    countList_POS = {doc.vocab[k].text: v for k, v in count_raw_POS.items() if doc.vocab[k].text in [\
                     'ADJ','ADP','ADV','DET','NOUN','PROPN','PRON','VERB']}
    #Total number of POS
    nPOS = sum([v for k, v in count_raw_POS.items()])
    #We check variety of POS
    pos_diversity = len(countList_POS)
    
    #We count the NER attributes
    count_raw_NER = [ent.label_ for ent in doc.ents if ent.label_ in ["PER", "LOC", "ORG"]]
    countList_NER = {\
                     "PER": sum(map(lambda a: 1 if a=="PER" else 0, count_raw_NER)),\
                     "LOC": sum(map(lambda a: 1 if a=="LOC" else 0, count_raw_NER)),\
                     "ORG": sum(map(lambda a: 1 if a=="ORG" else 0, count_raw_NER))}
    
    #We count total number of words
    words = [token.text for token in doc if token.is_alpha]
    
    #We analyze sentiment
    text = Text(title.lower(), hint_language_code="es")

    vector = doc.vector
    
    #If we want to include pos_and_ner analysis
    pos_ner_array = [len(words), \
         round_prox(sum([len(word) for word in words])/len(words)),\
         round_prox(countList_POS.get('ADJ')/nPOS) if countList_POS.get('ADJ') else 0,\
         round_prox(countList_POS.get('ADP')/nPOS) if countList_POS.get('ADP') else 0,\
         round_prox(countList_POS.get('ADV')/nPOS) if countList_POS.get('ADV') else 0,\
         round_prox(countList_POS.get('DET')/nPOS) if countList_POS.get('DET') else 0,\
         round_prox(countList_POS.get('NOUN')/nPOS) if countList_POS.get('NOUN') else 0,\
         round_prox(countList_POS.get('PROPN')/nPOS) if countList_POS.get('PROPN') else 0,\
         round_prox(countList_POS.get('PRON')/nPOS) if countList_POS.get('PRON') else 0,\
         round_prox(countList_POS.get('VERB')/nPOS) if countList_POS.get('VERB') else 0,\
         round_prox(countList_NER.get('PER')/nPOS) if countList_NER.get('PER') else 0,\
         round_prox(countList_NER.get('LOC')/nPOS) if countList_NER.get('LOC') else 0,\
         round_prox(countList_NER.get('ORG')/nPOS) if countList_NER.get('ORG') else 0,\
         round_prox(pos_diversity/nPOS)]
    vector = numpy.concatenate((vector, pos_ner_array))
        
    #If we want to include sentiment analysis
    vector = numpy.concatenate((vector, [round_prox((text.polarity))]))
        
    return vector.reshape(1,-1)

class WordVectorizerPipeline(TransformerMixin, BaseEstimator):
    def __init__(self, model="es_core_news_lg"):
        self.model = model

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        #Evaluating if spacy spanish model exists
        nlp = spacy.load(self.model)
        #Evaluating if polyglot sentiment module exist
        try:
            text = Text("Evaluando existencia de sentiment2.es",hint_language_code="es").polarity
        except:
            #Destination where we will copy sentiment2 pickle
            #This code of exception is designed to work on google app engine with /code/ as python root
            #Comment it and install package manually for other platforms
            print("sentiment2 not found. Copying...")
            parent_dest=str(downloader.default_download_dir())

            if not os.path.isdir(parent_dest + "/sentiment2/es"):
                createdPath1=parent_dest+"/sentiment2/es"
                os.makedirs(createdPath1)

            copyfile(str(os.getcwd())+"/processing/es.sent.pkl.tar.bz2", createdPath1+"/es.sent.pkl.tar.bz2")
            print("copy finished")
        return numpy.concatenate([singleSampleProcessPipeline(doc, nlp) for doc in X])