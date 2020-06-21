from rest_framework import serializers
from .models import Price


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('price', 'date', 'weight')

    def create(self, validated_data):
        """
        Modify create function to check if the prices received correspond to a date that is already on DB.
        In these case assumed that lastest price is the correct one
        """
        date = validated_data['date']
        instance = Price.objects.filter(date=date).first()

        if instance:
            return super().update(instance, validated_data)
        else:
            return super().create(validated_data)