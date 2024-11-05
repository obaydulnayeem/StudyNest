from django.urls import path
from .views import *

urlpatterns = [
    path('submit/', submit_feedback, name='submit_feedback'),
    path('display/', display_feedbacks, name='display_feedbacks'),
]
