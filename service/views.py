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

        print(username, len(brain_signal))

        arr = feature_extractor.get_feature_signal(brain_signal)
        print(arr.shape)

        """
        feature = feature_extractor.get_feature_signal(brain_signal)
        try:
            models.UserData.objects.create(user_name= username,brain_signal=feature)
        except Exception as e:
            print(str(e))
            
        all_entries = models.UserData.objects.all().filter(user_name= username)            

        """

    return HttpResponse("<h1>Hello</h1>")


@csrf_exempt
def savedata_login(request):
    if request.method == "POST":
        #print(request.body)
        lst = request.body.decode("utf-8").split(",")
        username = lst[0]
        result = 1
        brain_signal = np.array(lst[1].split(" "))

        print(username, len(brain_signal))

        print(username, len(brain_signal))

        arr = feature_extractor.get_feature_signal(brain_signal)
        print(arr.shape)

        """
        feature = feature_extractor.get_feature_signal(brain_signal)
            
        all_entries = models.UserData.objects.all().filter(user_name= username)[0]  
        
        result = feature_extractor.NaiveBayes(train_arr, test_arr, train_size, test_size)   
        
        try:
            models.UserData.objects.create(user_name= username,brain_signal=feature)
        except Exception as e:
            print(str(e))       

        """
    return HttpResponse(str(result))


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