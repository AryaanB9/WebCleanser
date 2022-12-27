import sys
import numpy as np
from feature import FeatureExtraction
import os

#** For Removing the INFO, WARNING and ERROR messages of Tensorflow
#* 0 = all messages are logged (default behavior)
#* 1 = INFO messages are not printed
#* 2 = INFO and WARNING messages are not printed
#* 3 = INFO, WARNING, and ERROR messages are not printed
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow import keras

loaded_model = keras.models.load_model("../model/trainedModel")

def predict(test_url):
    obj = FeatureExtraction(test_url)
    x = np.array(obj.getFeaturesList()).reshape(1,30) 
    y_pred = loaded_model.predict(x)[0]
    return y_pred[0]

def main():
    url = sys.argv[1]
    # url = "http://phished.com/"
    prediction = predict(url)
    
    print("Checking URL : ", url);
    print("Safety % : "+str(prediction*100))
    if prediction <= 1 and prediction > 0.8:
        print("SAFE")
    elif prediction <= 0.8 and prediction > 0.2:
        print("SUSPICIOUS")
    else:
        print("MALICIOUS")

main()