from django.shortcuts import render
from django.http import JsonResponse
from register.models import *
from django.core.exceptions import ObjectDoesNotExist

def login(request):
    name = "NiCo"
    return render(request, 'login/login.html', locals())

def login_check(request):
    print("IMONLOGIN")
    return_dict = dict()

    data = request.POST
    email_from_form = data.get("email")
    password_from_form = data.get("password")

    print ("pass hash: ", password_from_form)

    try:
        User.objects.get(email=email_from_form)
        return_dict["login_pass"] = True
        return_dict["user_id"] = User.objects.get(email=email_from_form).id
    except ObjectDoesNotExist:
        return_dict["login_pass"] = False

    return JsonResponse(return_dict)