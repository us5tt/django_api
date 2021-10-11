from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView

from django.http import HttpResponse

from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return HttpResponse("Головна сторінка в розробці")


class ParsView(CreateAPIView, ListAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


