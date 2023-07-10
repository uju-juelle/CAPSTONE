from rest_framework import serializers
from .models import House, Booking


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ["name", "description", "address", "type", "price", "build_year", "agent"]
        #"__all__"
        #["name", "description", "address", "type", "price", "build_year", "agent"]



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"