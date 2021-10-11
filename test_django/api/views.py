from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from django.http import HttpResponse

from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return HttpResponse("main page coming soon")


class ParsView(ListCreateAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(RetrieveUpdateAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(RetrieveUpdateDestroyAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


