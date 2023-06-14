from django.contrib import admin
from django.urls import path
from progress.views import progress_view

urlpatterns = [
    path('', progress_view, name='progress')
]
