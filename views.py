from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime
from ColisVip.models import Announcement



""" vue qui affiche le signe de politesse"""
def home(request):
    return render_to_response("ColisVip/index.html")



"""Nous créeons une interface intéractive avec les donnes"""
