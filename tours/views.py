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
        data = request.data
        requested_quantity = data.pop('quantity')
        tour = Tour.objects.filter(**data).filter(full=False).filter(available__gte=requested_quantity)
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

@api_view(['GET', 'PUT'])
def tour_detail(request, tour_pk):
    try:
        tour = Tour.objects.get(pk = tour_pk)
    except Tour.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TourSerializer(tour, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        requested_quantity = request.data['quantity']
        available_quantity = tour.available
        if(requested_quantity <= available_quantity):
            tour.available -= requested_quantity
            if(tour.available == 0):
                tour.full = True
            tour.save()
            return Response(status = status.HTTP_200_OK)
        return Response(status = status.HTTP_403_FORBIDDEN)
        