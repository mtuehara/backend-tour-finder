from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Tour
from .serializers import *
from django.shortcuts import render
# Create your views here.

@api_view(['GET'])
def tour_list(request):
    if request.method == 'GET':
        tour = Tour.objects.all()
        serializer = TourSerializer(tour, context ={'request': request}, many = True)
        return Response({
            'data': serializer.data
        })

@api_view(['GET', 'POST'])
def tour_query(request):
    if request.method == 'GET':
        city = request.data.city
        tour_type = request.data.tour_type
        date = request.data.date
        tour = Tour.objects.filter(date).filter(city).filter(tour_type)
        serializer = TourSerializer(tour, context ={'request': request}, many = True)

        return Response({
            'data': serializer.data
        })
    elif request.method == 'POST':
        serializer = TourSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tour_detail(request, tour_pk):
  #Retrieve, update or delete a event by id/pk.
    try:
        tour = Tour.objects.get(pk = tour_pk)
    except Tour.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TourSerializer(tour, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TourSerializer(tour, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        