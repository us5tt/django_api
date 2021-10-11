from django.urls import path
from .views import ParsView, SingleParsView


app_name = "items"

urlpatterns = [
    path('items/', ParsView.as_view()),
    path('items/<int:pk>', SingleParsView.as_view())
]

