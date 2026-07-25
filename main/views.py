from django.shortcuts import render, redirect, get_object_or_404
from .forms import UrlForm, UnshortForm
from .models import UrlList
from .utils import getNewStr
import requests

# Create your views here.

def home(request):
    sessionInput = request.session.get('input_url', '')
    sessionOutput = request.session.get('output_url', '')
    savedurl = [sessionOutput, sessionInput]
    if sessionInput:
        request.session.clear()

    if request.method == "POST":
        form = UrlForm(request.POST)

        if form.is_valid():

            inputUrl = form.cleaned_data['input_url']
            keywords = form.cleaned_data['shorten']

            chars = getNewStr()
            if keywords:
                chars = keywords


            UrlList.objects.create(input_url= inputUrl, shorten = chars)
            savedurl = get_object_or_404(UrlList, shorten = chars)
            request.session['output_url'] = savedurl.shorten
            request.session['input_url'] = inputUrl
            return redirect('home')
    else:
        form = UrlForm()

    return render(request, 'main/index.html', {"form": form, "url": savedurl})

def visitShort(request, chars):
    if chars:
        value = UrlList.objects.get(shorten = chars)
        if not value:
            print('url does not exist')

        return redirect(value.input_url)
    

def unshort(request):
    sessionStatus = request.session.get('url_status', '')
    sessionUrl = request.session.get('original_url', '')
    urlData = [sessionStatus, sessionUrl]
    if sessionUrl:
        request.session.clear()

    if request.method == "POST":
        form = UnshortForm(request.POST)
        if form.is_valid():
            shortUrl = form.cleaned_data['url']

            response = requests.get(shortUrl)

            status = response.status_code
            url = response.url
            request.session['url_status'] = status
            request.session['original_url'] = url

            return redirect('unshortner')
    else:
        form = UnshortForm()

    return render(request, 'main/unshortner.html', {'form': form, "data": urlData})