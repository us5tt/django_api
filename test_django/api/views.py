from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


from django.http import HttpResponse

from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return HttpResponse("Головна сторінка в розробці")


class ParsView(ListCreateAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(RetrieveUpdateAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer

