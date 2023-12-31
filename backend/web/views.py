from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    return render(request=request, template_name="index.html")


@require_http_methods(["GET"])
def auth(request):
    return render(request=request, template_name="auth.html")


@require_http_methods(["GET"])
def profile(request):
    return render(request=request, template_name="profile.html")


def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response
