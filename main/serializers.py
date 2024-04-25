from rest_framework import serializers
from .models import Tuman, Maktab, Shaxs

class ShaxsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shaxs
        fields = '__all__'

class MaktabSerializer(serializers.ModelSerializer):
    shaxslar = ShaxsSerializer(many=True, read_only=True)

    class Meta:
        model = Maktab
        fields = '__all__'

class TumanSerializer(serializers.ModelSerializer):
    maktablar = MaktabSerializer(many=True, read_only=True)

    class Meta:
        model = Tuman
        fields = '__all__'
