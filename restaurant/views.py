from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .serializers import MenuItemSerializer, BookingItemSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


# from django.http import HttpResponse

from .forms import BookingForm
from django.core import serializers
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')






# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@api_view(["POST","GET"])
def test(request):
    return Response("test end point", status=status.HTTP_200_OK)

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_delivery(user):
    return user.groups.filter(name='Delivery crew').exists()

def is_customer(user):
    #Need to implement properly
    return True

class BookingItemView(APIView):
    def get(self, request):
        queryset = Booking.objects.all()
        serializer = BookingItemSerializer(queryset, many=True)
        return Response({'Bookings': serializer.data}, status=status.HTTP_200_OK)

class SingleMenuItemView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response({'MenuItems': serializer.data}, status=status.HTTP_200_OK)

class MenuItemView(APIView):
    def get(self, request):
        queryset = Menu.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response({'MenuItems': serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = MenuItemSerializer(data=request.POST.dict())
        if(serializer.is_valid()):
            serializer.save()
            return Response({'Message': "Successfully added"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({'Message': "Data validation error " + str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request):
        return Response({'Message': "Access denied"}, status=status.HTTP_403_FORBIDDEN)
    def delete(self, request):
        return Response({'Message': "Access denied"}, status=status.HTTP_403_FORBIDDEN)
    def put(self, request):
        return Response({'Message': "Access denied"}, status=status.HTTP_403_FORBIDDEN)

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingItemSerializer
    permission_classes = [IsAuthenticated]