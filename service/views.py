from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pickle
from django.views.decorators.csrf import csrf_exempt
import json
from service import models
from service import feature_extractor
import os


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello</h1>")

def test(request):
    return HttpResponse("<h1>test</h1>")

@csrf_exempt
def savedata_signup(request):
    if request.method == "POST":
        #print(request.body)

        lst = request.body.decode("utf-8").split(",")
        username = lst[0]
        brain_signal = np.array(lst[1].split(" "))

        arr = feature_extractor.get_feature_signal(brain_signal)

        filename = username
        if username == "":
            filename = "test.out"

        path = get_path(filename)

        np.savetxt(path, arr)
    return HttpResponse("<h1>Hello</h1>")


@csrf_exempt
def savedata_login(request):
    if request.method == "POST":
        lst = request.body.decode("utf-8").split(",")
        username = lst[0]
        result = 1
        brain_signal = np.array(lst[1].split(" "))

        arr = feature_extractor.get_feature_signal(brain_signal)

        if username == "":
            filename = "test.out"
        path = get_path(filename)

        array = np.loadtxt(path)

        result = feature_extractor.NaiveBayes(arr, array, len(arr), len(array))

    return HttpResponse(str(result))


def get_path(filename):
    path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'data', filename),
    )
    return path