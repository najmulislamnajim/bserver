from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import filters, pagination
from rest_framework import viewsets
from rest_framework.response import Response
from .models import DonorModel,DonationRequestModel
from .serializers import DonorSerializer,DonationRequestSerializer

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

# Create your views here.
class DonorPagination(pagination.PageNumberPagination):
    page_size = 9 # items per page
    page_size_query_param = page_size
    max_page_size = 100
    
class DonorViewSet(viewsets.ModelViewSet):
    queryset=DonorModel.objects.all()
    serializer_class=DonorSerializer
    pagination_class = DonorPagination
        
class DonationRequestViewSet(APIView):
    serializer_class=DonationRequestSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            patient=serializer.save()
            print(patient)
            print(patient.donor.email)
            email_subject = "new blood donate request"
            email_body = render_to_string('mail.html', {'data' :patient})
            
            email = EmailMultiAlternatives(email_subject , '', to=[patient.donor.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("success")
        return Response(serializer.errors)
    
