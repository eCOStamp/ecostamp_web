# from django.shortcuts import render
from django.http import HttpResponse
from core.models import Stamp
from django.contrib.auth import authenticate as auth
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
import json


@require_POST
def dummy(request):
    try:
        response = json.loads(request.body)  # Only available in POST request
        response["stamp_url"] = "http://ecostamp.naist.jp/static/img/stamp.jpg"
        response["name"] = "Matsumoto Castle"
        response["description"] = "Matsumoto castle is located somewhere in Japan..."
        response["url"] = "http://www.japanese-castle-explorer.com/castle_profile.html?name=Matsumoto"
        response["success"] = True
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    except TypeError as e:
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


def stamp(request, key):
    try:
        key = key.lower()
        stamp = Stamp.objects.get(key=key)
        response = dict()
        response["image_url"] = stamp.image_url
        response["name"] = stamp.name
        response["short_description"] = stamp.short_description
        response["description"] = stamp.description
        response["url"] = stamp.url
        response["success"] = True
    except Stamp.DoesNotExist as e:
        response = {"success": False, "reason": str(e)}
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    except TypeError as e:
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


@require_POST
def register(request):
    try:
        parsed = json.loads(request.body)  # Only available in POST request
        User.objects.create_user(parsed["username"], parsed["email"], parsed["password"])
        response = {"success": True}
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


@require_POST
def collect(request):
    try:
        parsed = json.loads(request.body)  # Only available in POST request
        user = User.objects.get(username=parsed["username"])
        stamp = Stamp.objects.get(key=parsed["key"].lower())
        user.stamp_set.add(stamp)
        user.save()
        response = {"success": True}
    except User.DoesNotExist as e:
        response = {"success": False, "reason": str(e)}
    except Stamp.DoesNotExist as e:
        response = {"success": False, "reason": str(e)}
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


def user(request, username):
    try:
        user = User.objects.get(username=username)
        response = {"username": user.username}
        response["stamps"] = list()
        for stamp in user.stamp_set.all():
            response["stamps"].append({
                "name": stamp.name,
                "description": stamp.description,
                "short_description": stamp.short_description,
                "url": stamp.url,
                "image_url": stamp.image_url,
            })
        response = {"success": True}
    except User.DoesNotExist as e:
        response = {"success": False, "reason": str(e)}
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


@require_POST
def authenticate(request):
    try:
        parsed = json.loads(request.body)  # Only available in POST request
        user = auth(username=parsed["username"], password=parsed["password"])
        if user is None:
            response = {"success": False, "reason": "The username and password were incorrect."}
        elif not user.is_active:
            response = {"success": False, "reason": "The password is valid, but the account has been disabled!"}
        else:
            response = {"success": True}
    except User.DoesNotExist as e:
        response = {"success": False, "reason": str(e)}
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))
