import tensorflow as tf
## Load the data to get started
import pandas as pd
import numpy as np
import tensorflow as tf
import spacy
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re
import keras
import string
import pickle


# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template,request
app = Flask(__name__)




#loading model 


model = pickle.load(open('static\\svc_pipe_model.sav', 'rb'))


# preprocessing text
def data_cleaning (text):
    text= re.sub(r"@\S+", '', text )
    text=re.sub(r"htt\S+", '', text )
    text=re.sub(r'ه{3,}','ههه', text )
    text=re.sub(r"^ +", '', text )
    text=re.sub(r" +$", '', text )
    text=re.sub(r"[a-zA-Z]+", ' ', text )

    text=re.sub(r"\n+", ' ', text )
    text=re.sub(r"[-+*><&%$#=@/^/[/|\]/{}()!\\?؟'\"،:~;.,_÷]+", ' ', text )
    text=re.sub(r"\d+", ' ', text )
    text=re.sub(r"[.]+", ' ', text )

    EMOJI_PATTERN = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)

    text=EMOJI_PATTERN.sub( r'', text )

    text=re.sub(r" {2,}", ' ', text )

    return text



def prediction(tweet):
    model.classes_

    tweet = data_cleaning(tweet)
    

    pred = model.predict(tweet)
   
    print(pred)
    return (model.classes_[pred])

# model.predict




@app.route('/')
def hello_world():
    return render_template('index.html')
   

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        glon = request.form['tweet']
        glon = prediction(glon)
        return render_template('index.html', prediction_text=glon)

if __name__ == '__main__':
    app.run()
