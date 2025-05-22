from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
    