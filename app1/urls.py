from django.urls import path
from app1.views import *

urlpatterns = [
    path('generate/', generate_otp, name="generate_otp"),
    path('verify/', verify_otp,  name="verify_otp"),
    
]
