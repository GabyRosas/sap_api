from rest_framework import serializers
from people.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person

        #Serializacion de la data
        fields = '__all__'
