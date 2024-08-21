from rest_framework import viewsets
from .serializer import PersonSerializer
from .models import Person

# Create your views here.

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    #usar modelo a través del ORM
    queryset = Person.objects.all()

