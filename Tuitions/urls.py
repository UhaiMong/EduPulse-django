from django.urls import path
from .views import TuitionView
urlpatterns = [
    path('courses/', TuitionView.as_view(), name='courses')
]
