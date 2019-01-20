from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from .models import Cards
from .serializers import CardSerializer
import requests
import random
import json

class ListCardView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    def get(self,request):
        queryset = self.get_queryset()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        queryset = self.get_queryset()
        serializer = CardSerializer(queryset, many=True)
        inDeck = 0
        sameOrNeutralCards = []
        random.shuffle(serializer.data)
        print(serializer.data)
        for card in serializer.data:
            if inDeck < 30:
                if "player_class" in card:
                    if card["player_class"] == request.data["playerClass"] or card["player_class"] == "Neutral":
                        foundInDeck = list(filter(lambda x: x["dbf_id"] == card["dbf_id"], sameOrNeutralCards))
                        if len(foundInDeck) < 2:
                            sameOrNeutralCards.append({"dbf_id": card["dbf_id"], "name": card["name"], "player_class": card["player_class"]})
                            inDeck += 1
            else:
                break
        return Response(sameOrNeutralCards)

class DeckView(APIView):    
    def post(self, request):
        url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble'
        headers = {'X-Mashape-Key': 'ZTMJtzbYvXmshPTFEZI4ztIy3I68p1nPwgHjsnIGukKZeJxGcs'}
        response = requests.get(url, headers=headers)
        allCards = response.json()
        inDeck = 0
        sameOrNeutralCards = []
        random.shuffle(allCards)
        for card in allCards:
            if inDeck < 30:
                if "playerClass" in card:
                    if card["playerClass"] == request.data["playerClass"] or card["playerClass"] == "Neutral":
                        foundInDeck = list(filter(lambda x: x["dbf_id"] == card["dbfId"], sameOrNeutralCards))
                        if len(foundInDeck) < 2:
                            sameOrNeutralCards.append({"dbf_id": card["dbfId"], "name": card["name"], "player_class": card["playerClass"]})
                            inDeck += 1
            else:
                break
        return Response(sameOrNeutralCards)