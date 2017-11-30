from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pickle
from django.views.decorators.csrf import csrf_exempt
import json
from service import models

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello</h1>")

def test(request):
    return HttpResponse("<h1>test</h1>")

@csrf_exempt
def savedata_signup(request):
    if request.method == "POST":
        print(request.body)

        """
        lst = request.body.split(",")
        username = lst[0]
        brain_signal = lst[1]
        models.UserData.objects.create(user_name= username,brain_signal=brain_signal)
        """

    return HttpResponse("<h1>Hello</h1>")


@csrf_exempt
def savedata_login(request):
    if request.method == "POST":
        print(request.body)

        """
        lst = request.body.split(",")
        username = lst[0]
        brain_signal = lst[1]
        models.UserData.objects.create(user_name=username, brain_signal=brain_signal)
        """
    return HttpResponse("<h1>Hello</h1>")


    """
    name = request.GET.get("name")
    email = request.GET.get("email")
    signal = request.GET.get("signal")

    file = name + ".pkl"
    signal_list = signal.split(" ")
    results = list(map(int, signal_list))
    np_data = np.array(results)


    pkl_file = open(file, 'rb')
    gnb = pickle.loads(pkl_file)
    pkl_file.close()

    value = gnb.predict(np_data)
    print(value)
    """





# import pickle
# s = pickle.dumps(clf)
# clf2 = pickle.loads(s)
# clf2.predict(X[0:1])