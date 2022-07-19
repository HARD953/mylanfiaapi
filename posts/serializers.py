from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localite
        fields = '__all__'

class PostAffectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affecter
        fields ='__all__'

class PostConjointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conjoint
        fields ='__all__'

class PostChefMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef_menage
        fields ='__all__'

class EmigrationS(serializers.ModelSerializer):
    class Meta:
        model = Emigration
        fields ='__all__'

class RecensementS(serializers.ModelSerializer):
    class Meta:
        model = Recenser
        fields ='__all__'

class EnfantS(serializers.ModelSerializer):
    class Meta:
        model = Enfant
        fields ='__all__'

class CommoditeS(serializers.ModelSerializer):
    class Meta:
        model = Commodite
        fields ='__all__'

class EquipementS(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields ='__all__'

class MigrantS(serializers.ModelSerializer):
    class Meta:
        model = Migrant
        fields ='__all__'

class DeceS(serializers.ModelSerializer):
    class Meta:
        model = Deces
        fields ='__all__'
