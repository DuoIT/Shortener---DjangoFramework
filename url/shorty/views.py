from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import shortyURL
from .forms import submitURLForm
from analytics.models import ClickEvent
# Create your views here.


# def shorty_re_view(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(shortyURL, shortcode=shortcode)
#     # return HttpResponse('Hello {sc}'.format(sc=obj))
#     return HttpResponseRedirect(obj.url)

def home_view(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'shorty/home.html', {})


class homeView(View):
    def get(self, request, *args, **kwargs):
        the_form = submitURLForm()
        context = {
             "title": "Enter your link here !!!",
             "form": the_form
         }
        return render(request, 'shorty/home.html', context)

    def post(self, request, *args, **kwargs):
        form = submitURLForm(request.POST)
        # context = {
        #     'title': "Submit URL",
        #     'form': form
        # }
        # template = 'shorty/home.html'
        if form.is_valid():
            print(form.cleaned_data.get('url'))
            new_url = form.cleaned_data.get('url')
            obj, created = shortyURL.objects.get_or_create(url=new_url)
        context = {
            "object": obj,
            "created": created,
        }
        if created:
            template = 'shorty/result.html'
        else:
            template = 'shorty/exits.html'
        return render(request, template, context)


class shortyReditectClassReView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        # qs = shortyURL.objects.filter(shortcode__iexact=shortcode)
        # print(qs)
        obj = get_object_or_404(shortyURL, shortcode=shortcode)
        print(obj)
        # if qs.count() != 1 and not qs.exists():
        #     raise Http404
        # obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
    # def post(self, request):
    #     return HttpResponse('admin post method')


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