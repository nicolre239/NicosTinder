from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from datetime import datetime

def register(request):
    name = "NiCo"
    return render(request, 'register/register.html', locals())

def reg_check(request):
    print("IMONREGCHECK")
    return_dict = dict()

    number_at_start = User.objects.count();
    print("numberatstart: ", number_at_start)

    data = request.POST
    email_from_form = data.get("email")
    name_from_form = data.get("name")
    password_from_form = data.get("password")
    sex_from_form = data.get("sex")
    age_from_form = data.get("age")

    if sex_from_form == "female":
        looking_sex = "male"
    else:
        looking_sex = "female"


    print(age_from_form)
    print ("pass hash: ", password_from_form)


    if int(age_from_form) >= 18:
        User.objects.get_or_create(email=email_from_form, defaults={'name': name_from_form, 'password_hash': password_from_form, 'sex': sex_from_form, 'age': age_from_form, 'looking_sex': looking_sex})

    number_at_end = User.objects.count();
    print("numberatendt: ", number_at_end)

    if number_at_start == number_at_end:
        return_dict["already_exsists"] = True
    else:
        return_dict["already_exsists"] = False
        return_dict["user_id"] = User.objects.get(email=email_from_form).id

    return JsonResponse(return_dict)