# from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson as json


def dummy(request):
    try:
        response = json.loads(request.body)
        response["success"] = True
        response["stamp_url"] = "http://ecostamp.naist.jp/static/img/stamp.jpg"
        response["name"] = "Matsumoto Castle"
        response["description"] = "Matsumoto castle is located somewhere in Japan..."
        response["url"] = "http://www.japanese-castle-explorer.com/castle_profile.html?name=Matsumoto"
    except json.JSONDecodeError as e:
        response = {"success": False, "reason": str(e)}
    except TypeError as e:
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))

