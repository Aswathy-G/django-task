import json

from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from posts.models import Post


def allow_self(function):
    def wrapper(request, *args, **kwargs):
        if not Post.objects.filter(id=id, author__user=request.user).exists():
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status":"error",
                    "title":"unauthorized access",
                    "message":"unauthorized access"
                }
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                return HttpResponseRedirect(reverse("web:index"))

        return function(request, *args, **kwargs)

    return wrapper
