from rest_framework import serializers
from .models import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('pk', 'name', 'date', 'full', 'city', 'capacity', 'available', 'tour_type', 'meeting_point')
        