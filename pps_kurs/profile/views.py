from django.shortcuts import render
from django.http import JsonResponse
from register.models import *

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profile/profile.html', locals())

def profile_watch(request, match_id, user_id):
    user = User.objects.get(id=match_id)
    return render(request, 'profile/profile_watch.html', locals())


def profile_change(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'profile/profile_change.html', locals())

def changes_save(request):
    return_dict = dict()

    data = request.POST
    name_from_form = data.get("name")
    description_from_form = data.get("description")
    ageFrom_from_form = data.get("ageFrom")
    ageTo_from_form = data.get("ageTo")
    sexFind_from_form = data.get("sexFind")
    user_id = data.get("id")

    user = User.objects.get(id=user_id)

    user.name = name_from_form
    user.description = description_from_form
    user.looking_age_from = ageFrom_from_form
    user.lookin_age_to = ageTo_from_form
    user.looking_sex = sexFind_from_form
    print(sexFind_from_form)
    user.save()

    print("IMONSAVE")
    return JsonResponse(return_dict)
