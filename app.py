from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
#import sklearn.externals.joblib as extjoblib
import joblib
import pickle
import pickle
clf = pickle.load(open('webmd.pkl','rb'))



# load the model from disk

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():


	if request.method == 'POST':
		message = request.form['prognosis']
		dat = [message]
		
		my_prediction = clf.predict(x_test)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
