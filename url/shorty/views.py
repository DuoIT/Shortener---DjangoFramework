from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import shortyURL
# Create your views here.


def shorty_re_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(shortyURL, shortcode=shortcode)
    # return HttpResponse('Hello {sc}'.format(sc=obj))
    return HttpResponseRedirect(obj.url)


class shortyClassReView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(shortyURL, shortcode=shortcode)
        return HttpResponse('Hi {sc}'.format(sc=obj))

    def post(self, request):
        return HttpResponse('admin post method')


'''
def shorty_re_view(request, shortcode=None, *args, **kwargs):
    # print(request.user)
    # print(request.user.is_authenticated())
    # print(args)
    # print(kwargs)
    print(request.method)
    # try:
    #     obj = shortyURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = shortyURL.objects.all().first()
    obj = get_object_or_404(shortyURL, shortcode=shortcode)
    # obj_url = obj.url
    # obj_url = None
    # qs = shortyURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    return HttpResponse('Hello {sc}'.format(sc=obj))
    
class shortyClassReView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        # print(args)
        # print(kwargs)
        print(request.method)
        obj = get_object_or_404(shortyURL, shortcode=shortcode)
        return HttpResponse('Hi {sc}'.format(sc=obj))

    def post(self, request):
        return HttpResponse('admin post method')
'''