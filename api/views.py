# from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson as json


def dummy(request):
    try:
        response = json.loads(request.body)
        response["success"] = True
    except json.JSONDecodeError as e:
        response = {"success": False, "reason": str(e)}
    return HttpResponse(json.dumps(response))
