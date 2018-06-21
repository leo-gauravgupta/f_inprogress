from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django import forms
import requests
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
#from .forms import UserRegistrationForm

#from .models import Topping, Menu, Order, Customer

# Create your views here.

#Index page, for authentication and appropriate routing to login / registration / menu:
def index(request):


    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=1min&apikey=4LGYQ85VR5EGTT7C'
    stock_results = requests.get(url)
    stock_results_json = stock_results.json()

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N)+5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N)-5

    # Create traces
    trace0 = go.Scatter(
        x = random_x,
        y = random_y0,
        mode = 'lines',
        name = 'lines'
    )
    trace1 = go.Scatter(
        x = random_x,
        y = random_y1,
        mode = 'lines+markers',
        name = 'lines+markers'
    )
    trace2 = go.Scatter(
        x = random_x,
        y = random_y2,
        mode = 'markers',
        name = 'markers'
    )
    data = [trace0, trace1, trace2]

    py.iplot(data, filename='line-mode')

    context = {
    #"stock_results": stock_results_json
    "stock_results": plot_sample
    }
    return render(request, "tickers/index.html", context)
