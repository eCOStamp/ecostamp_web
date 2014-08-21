# from django.shortcuts import render
from django.http import HttpResponse
from core.models import Stamp
import json


def dummy(request):
    try:
        response = json.loads(request.body)  # Only available in POST request
        response["success"] = True
        response["stamp_url"] = "http://ecostamp.naist.jp/static/img/stamp.jpg"
        response["name"] = "Matsumoto Castle"
        response["description"] = "Matsumoto castle is located somewhere in Japan..."
        response["url"] = "http://www.japanese-castle-explorer.com/castle_profile.html?name=Matsumoto"
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    except TypeError as e:
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


def stamp(request, key):
    try:
        print key
        stamp = Stamp.objects.get(key=key)
        response = dict()
        response["success"] = True
        response["image_url"] = stamp.image_url
        response["name"] = stamp.name
        response["short_description"] = stamp.short_description
        response["description"] = stamp.description
        response["url"] = stamp.url
    except Stamp.DoesNotExist as e:
        response = {"success": False, "reason": str(e)}
    except ValueError as e:  # Bad json
        response = {"success": False, "reason": str(e)}
    # except TypeError as e:
    #     response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))


def register(request):
    # TODO: Write me
    pass
