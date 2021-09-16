from django.db.models import fields
from rest_framework import serializers
from store.models import *

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id','Name')


class StoreDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreContent
        fields = ('Product','Count')

class StoreDetailAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreAddProduct
        fields = ('Store','Product','Count')

class StoreDetailBuySerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreBuyProduct
        fields = ('Store','Product','Count')