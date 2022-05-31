import csv
import io
import json
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import Customer, User
from rest_framework import status, generics

from accounts.serializers import UserSerializer


# Create your views here.

# class UserFormApiView(APIView):
    
    
#     def get(self, request, *args, **kwargs):
#         with open('pillar.csv', mode ='r')as file:
   
#             # reading the CSV file
#             csv_file = csv.DictReader(file)
#             data = {}
#             count = 0

#             # displaying the contents of the CSV file
#             for lines in csv_file:
#                 data[count] = lines
#                 count+=1
#             _, created = User.objects.get_or_create(
#                 data=data
#             )
            
#             # print(created.data)
#             return Response({"status": "success"},
#                             status.HTTP_201_CREATED)



#create form template api
class UserFormApiView(APIView):
    
    def post(self, request, *args, **kwargs):
        data = []
        count=0
        file = request.FILES['csv_file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        for row in reader:
            data.append(row)
            count+=1
        created = User.objects.create(
            data=data
        )
      
        return Response(created.data, status.HTTP_201_CREATED)


# user create form api
class UserFormCreateApiView(APIView):
    
    def post(self, request, *args, **kwargs):
        # data = json.loads(request.POST.dict().keys()[0])  
        data = json.dumps(request.data) 
        created = Customer.objects.create(
            user_form = data
        )
      
        return Response(created.user_form, status.HTTP_201_CREATED)


# user update and delete this form
class UserUpdateApiView(APIView):
  
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        data=user.user_form
        return Response(json.loads(data))


    def put(self, request, pk, *args, **kwarg):
        instance = self.get_object(pk)
        data = json.dumps(request.data) 
        instance.user_form = data
        instance.save()
        data = {'message': 'data Updated Successfully',}
        return Response(data, status=status.HTTP_201_CREATED)
        

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

