import requests
from urllib.parse import urlparse
from user_agents import parse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UrlForm, UnshortForm
from .models import UrlList
from .utils import getNewStr, getClientIp, getDevice
from analytics.models import Visit

# Create your views here.

def home(request):
    sessionInput = request.session.get('input_url', '')
    sessionOutput = request.session.get('output_url', '')
    savedurl = [sessionOutput, sessionInput]

    request.session.pop('input_url', None)
    request.session.pop('output_url', None)

    if request.method == "POST":
        form = UrlForm(request.POST)

        if form.is_valid():

            inputUrl = form.cleaned_data['input_url']
            keywords = form.cleaned_data['shorten']
            title = form.cleaned_data['title']

            chars = keywords if keywords else getNewStr()
            creator = None
            if request.user.is_authenticated:
                creator = request.user

            UrlList.objects.create(input_url=inputUrl, shorten=chars, created_by=creator, title=title)
            savedurl = get_object_or_404(UrlList, shorten = chars)
            request.session['output_url'] = savedurl.shorten
            request.session['input_url'] = inputUrl
            return redirect('home')
    else:
        form = UrlForm()

    return render(request, 'main/index.html', {"form": form, "url": savedurl, 'base_url': request.build_absolute_uri("/").rstrip("/")})

def visitShort(request, chars):
    if chars:
        link = UrlList.objects.get(shorten = chars)
        if not link:
            print('url does not exist')

        ua = parse(request.META.get('HTTP_USER_AGENT', ''))

        Visit.objects.create(
            url=link,
            referrer=request.META.get('HTTP_REFERRER'),
            ip_address=getClientIp(request),
            browser=ua.browser.family,
            os=ua.os.family,
            device_type=getDevice(ua),
            is_bot=ua.is_bot,
        )
        return redirect(link.input_url)
    

def unshort(request):
    sessionStatus = request.session.get('url_status', '')
    sessionUrl = request.session.get('original_url', '')
    urlData = [sessionStatus, sessionUrl]

    request.session.pop('url_status', None)
    request.session.pop('original_url', None)
        
    if request.method == "POST":
        form = UnshortForm(request.POST)
        if form.is_valid():
            baseUrl = request.build_absolute_uri("/").rstrip("/")
            shortUrl = form.cleaned_data['url']

            current = urlparse(baseUrl)
            target = urlparse(shortUrl)

            if current.netloc == target.netloc:

                code = shortUrl.rstrip('/').split('/')[-1]
                link = UrlList.objects.get(shorten=code)

                request.session['url_status'] = '200'
                request.session['original_url'] = link.input_url

                return redirect('unshortner')
            
            response = requests.get(shortUrl)

            status = response.status_code
            url = response.url
            request.session['url_status'] = status
            request.session['original_url'] = url

            return redirect('unshortner')
    else:
        form = UnshortForm()

    return render(request, 'main/unshortner.html', {'form': form, "data": urlData})

@login_required
def edit_url(request, id):
    url = UrlList.objects.get(id=id)

    if request.method == "POST":
        form = UrlForm(request.POST, instance=url)

        if form.is_valid():
            form.save()
            return redirect('link_details', url_id=url.id)
        
    else:
        form = UrlForm(instance=url)

    return render(request, 'main/edit.html', {'url':url, 'form': form})

@login_required
def change_status(request, id):
    if request.method != "POST":
        return redirect('dashboard')

    url = get_object_or_404(UrlList, id=id)

    url.status = 'active' if url.status == 'disabled' else 'disabled'
    url.save()
    return redirect('dashboard')

