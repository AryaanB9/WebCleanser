import warnings
import joblib
# import feature
import sys
import numpy as np
import pickle
from feature import FeatureExtraction
from feature import MODEL_PATH
from tensorflow import keras

pickle_model = keras.models.load_model('C:/xampp/htdocs/DJ22Trial3/train/mymodel1')

# file = open("D:/DevJams2022/Trial2/model.pkl","rb")
# pickle_model = pickle.load(open("C:/xampp/htdocs/DJ22Trial3/model3.pkl","rb"))
# filename = 'model4'
# pickle_model = joblib.load(MODEL_PATH)
# file.close()

def predict(test_url):

    obj = FeatureExtraction(test_url)
    x = np.array(obj.getFeaturesList()).reshape(1,30) 

    y_pred = pickle_model.predict(x)[0]

    # 1 is safe
    # -1 is unsafe

    # y_pro_phishing = pickle_model.predict_proba(x)[0,0]
    # y_pro_non_phishing = pickle_model.predict_proba(x)[0,1]
    # if(y_pred ==1 ):
    # pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)

    return y_pred[0]
    # return x


def main():
    url = sys.argv[1]
    
    prediction = predict(url)
    # print("Prediction : "+str(prediction))
    # features = featureExtract(url)
    if prediction <= 1 and prediction > 0.5:
        print("SAFE")
    elif prediction <= 0.5 and prediction > 0.1:
        print("SUSPICIOUS")
    else:
        print("PHISHING")
    # print(features)

main()
