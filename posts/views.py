from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
# Create your views here.

class WritePermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id==request.user
        
class PostList(generics.ListCreateAPIView):
    queryset=Localite.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer
  
class PostDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Localite.objects.all()
    serializer_class=PostSerializer

class AffecterList(generics.ListCreateAPIView):
    queryset=Affecter.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostAffectationSerializer
  
class AffecterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[WritePermission]
    queryset=Affecter.objects.all()
    serializer_class=PostAffectationSerializer


class ConjointList(generics.ListCreateAPIView):
    queryset=Conjoint.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostConjointSerializer
  
class ConjointDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Affecter.objects.all()
    serializer_class=PostConjointSerializer

class ChefMenageList(generics.ListCreateAPIView):
    queryset=Chef_menage.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=PostChefMSerializer
  
class ChefMenageDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Chef_menage.objects.all()
    serializer_class=PostChefMSerializer

class EmigrationList(generics.ListCreateAPIView):
    queryset=Emigration.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=EmigrationS
  
class EmigrationDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Emigration.objects.all()
    serializer_class=EmigrationS

class RecenserList(generics.ListCreateAPIView):
    queryset=Recenser.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=RecensementS
  
class RecenserDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Recenser.objects.all()
    serializer_class=RecensementS


class EnfantList(generics.ListCreateAPIView):
    queryset=Enfant.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=EnfantS
  
class EnfantDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Enfant.objects.all()
    serializer_class=EnfantS

class CommoditeList(generics.ListCreateAPIView):
    queryset=Commodite.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=CommoditeS
  
class CommoditeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Commodite.objects.all()
    serializer_class=CommoditeS

class EquipementList(generics.ListCreateAPIView):
    queryset=Equipement.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=EquipementS
  
class EquipementDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Equipement.objects.all()
    serializer_class=EquipementS

class MigrantList(generics.ListCreateAPIView):
    queryset=Migrant.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=MigrantS
  
class MigrantDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Migrant.objects.all()
    serializer_class=MigrantS

class DecesList(generics.ListCreateAPIView):
    queryset=Deces.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=DeceS
  
class DecesDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[WritePermission]
    queryset=Deces.objects.all()
    serializer_class=DeceS


class RecensementView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data = JSONParser().parse(request)
        if data['Chef_menage']:
            serializerch = PostChefMSerializer(data=data['Chef_menage'])
        if data['Conjoint']:
            serializerco = PostConjointSerializer(data=data['Conjoint'])
        if data['Emigration']:
            serializeremi = EmigrationS(data=data['Emigration'])
        if data['Recenser']:
            serializerr = RecensementS(data=data['Recenser'])
        if data['Enfant']:
            serializere=EnfantS(data=data['Enfant'])
        if data['Commodite']:
            serializerc=CommoditeS(data=data['Commodite'])
        if data['Equipement']:
            serializereq=EquipementS(data=data['Equipement'])
        if data['Migrant']:
            serializerm=MigrantS(data=data['Migrant'])
        if data['Deces']:
            serializerd=DeceS(data=data['Deces'])
        if serializereq.is_valid() and serializerch.is_valid() and serializerco.is_valid() and serializeremi.is_valid() and serializerc.is_valid() and serializere.is_valid() and serializerm.is_valid() and serializerd.is_valid():
            serializerch.save()
            serializerco.save()
            serializeremi.save()
            serializerr.save()
            serializere.save()
            serializerc.save()
            serializereq.save()
            serializerm.save()
            serializerm.save()
            return JsonResponse(serializerp.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    # def get(self,request,pk):
    #     try:
    #         affectations = Affecter.objects.get(pk=pk)
    #     except affectations.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer = PostAffectationSerializer(affectations)
    #     return JsonResponse(serializer.data)

 