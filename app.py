# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:23:00 2021

@author: Amaan
"""
#importing modules
from flask import Flask, request,render_template
import numpy as np
import re
import requests
import json
import os
from gevent.pywsgi import WSGIServer
#App Definition
app=Flask(__name__)

#Output Function
def check(output):
    url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"
    querystring = {"image_url":output,"sourceType":"url"}
    headers = {
    'x-rapidapi-key': "########", #enter uniquie API key
    'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
    }
    response = requests.request("POST", url, headers=headers, params=querystring)
    print(response.text)
    return response.json()["results"][0]["plate"],response.json()["results"][0]["confidence"]

#Routing Pages

#Home Page
@app.route('/')
def home():
    return render_template('base.html')

#Prediction Page
@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    plate,conf=check(output)
    return render_template('base.html',output=plate+" with a confidence score of "+str(round(conf))+"%")

#Main Function
if __name__=="__main__":
    app.run(debug=True)
