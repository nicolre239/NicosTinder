from django.shortcuts import render
from django.http import JsonResponse
from register.models import *
from django.core.exceptions import ObjectDoesNotExist
from numpy import array

def likes(request, user_id):
    user = User.objects.get(id=user_id)
    matches_array = []*1
    matchnames_array = []*1

    if user.paired_ids != None:
        for i, match_id in enumerate (user.paired_ids.split(',')):
            matches_array.append(User.objects.get(id=match_id))

    matches_count = len(matches_array)
    print(matches_array)
    return render(request, 'likes/matches.html', locals())

def search_pairs(request, user_id):
    user = User.objects.get(id=user_id)
    pairs_list = User.objects.filter(sex=user.looking_sex)
    pairs_list = pairs_list.filter(age__gte=user.looking_age_from)
    pairs_list = pairs_list.filter(age__lte=user.lookin_age_to)
    pairs_list = pairs_list.filter(looking_sex=user.sex)
    pairs_list = pairs_list.exclude(id=user_id)

    pairs_count = len(pairs_list)
    return render(request, 'likes/pairs.html', locals())

def delete_like(request):
    return_dict = dict()
    data = request.POST
    user_id = data.get("user_id")
    match_id = data.get("match_id")

    print("ONDELETE" + user_id + "   " + match_id)

    user = User.objects.get(id=user_id)
    match = User.objects.get(id=match_id)

    temp = user.paired_ids.replace(match_id,"")
    temp = temp.replace(",,",",")

    if len(temp) != 0:
        if temp[0] == ",":
            temp = temp[1:]
        if temp[len(temp) - 1] == ",":
            temp = temp[:len(temp) - 1]

    user.paired_ids = temp
    user.save()

    temp = match.paired_ids.replace(user_id, "")
    temp = temp.replace(",,", ",")

    if len(temp) != 0:
        if temp[0] == ",":
            temp = temp[1:]
        if temp[len(temp) - 1] == ",":
            temp = temp[:len(temp) - 1]

    match.paired_ids = temp
    match.save()

    if user.banned_ids == None:
        user.banned_ids = match.id
        user.save()
    else:
        user.banned_ids = str(user.banned_ids) + "," + str(match.id)
        user.save()
        
    if match.banned_ids == None:
        match.banned_ids = user.id
        match.save()
    else:
        match.banned_ids = str(match.banned_ids) + "," + str(user.id)
        match.save()

    if len(user.paired_ids) == 0:
        print("user0")
        user.paired_ids = None
        user.save()
    if len(match.paired_ids) == 0:
        print("match0")
        match.paired_ids = None
        match.save()
    return JsonResponse(return_dict)