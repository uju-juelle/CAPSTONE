from django.shortcuts import render
from rest_framework.views import APIView
from .models import House, Booking
from .serializers import HouseSerializer, BookingSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter

class House_homepage(APIView):
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ["type"]
    def get(self, request):
        all_houses = House.objects.all()
        serializer = HouseSerializer(all_houses, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class Create_page(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "New House Added",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response("Invalid data entered")
    

class house_detailpage(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id):
        detail = House.objects.get(id=id)
        serializer = HouseSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Booking_page(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        houses = Booking.objects.all()
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Booking.objects.create(name=name, )
            return Response({"success": "successful booking", 
                             "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
    


















# class api_homepage(APIView):
#     def get(self, request, id):
#          detail = Post.objects.get(id=id)
#          new_serializer = PostSerializer(detail)
#          return Response(new_serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#           serializer = PostSerializer(data=request.data)
#           if serializer.is_valid():
#             serializer.save()
#             return Response({"success": "Nice Work!!",
#                             "data": serializer.data}, status=status.HTTP_201_CREATED)
#           return Response("invalid data entered")
    


# class api_detailpage(APIView):
#     def get(self, request, id):
#          detail = Post.objects.get(id=id)
#          new_serializer = PostSerializer(detail)
#          return Response(new_serializer.data, status=status.HTTP_200_OK)

#     def put(self,request, id):
#         detail = Post.objects.get(id=id)
#         serializer = PostSerializer(detail, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#     def delete(self,request, id):
#         detail = Post.objects.get(id=id)
#         detail.delete()
#         return Response("Post has been deleted", status=status.HTTP_204_NO_CONTENT)

