from django.contrib.auth.models import User, Group
from .models import Cards
from rest_framework import serializers


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cards
        fields = ('dbf_id', 'player_class', 'name')