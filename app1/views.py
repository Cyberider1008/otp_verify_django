from django.shortcuts import render,redirect
import pyotp

# Create your views here.

totp = pyotp.TOTP('base32secret3232', interval=120)
        

def generate_otp(request):
    if request.method =="POST":
        number = request.POST['mobile_number']
        print(number)
        current_otp = totp.now()
        print(current_otp)
        request.session['number'] = number
        request.session['current_otp'] = current_otp
        

    return render(request, 'generate_otpPage.html')



def verify_otp(request):
    current_otp = request.session['current_otp'] 
    number = request.session['number']
    print("request..........")
    if request.method == "POST":
        otp = request.POST['otp']
        print("c",otp)
        if totp.verify(otp):
            print("ok good")
            request.session.clear()
        else:
            print("not")

    return render(request, 'verify_otpPage.html',{'current_otp':current_otp, 'number':number})
