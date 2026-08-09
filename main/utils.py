import secrets
import string
from .models import UrlList

CHARATERS = string.ascii_letters + string.digits

def getRandomChars():
    chars = ''
    for _ in range(6):
        chars += secrets.choice(CHARATERS)
    
    return chars


def getNewStr():
    while True:
        chars = getRandomChars()
        exist = UrlList.objects.filter(shorten = chars)

        if not exist:
            return chars


def getClientIp(request):
    forward = request.META.get("HTTP_X_FORWARDED_FOR")

    if forward:
        return forward.split(',')[0].strip()

    return request.META.get("REMOTE_ADDR")

def getDevice(ua):
    if ua.is_mobile:
        device="Mobile"
    elif ua.is_pc:
        device="Desktop"
    elif ua.is_tablet:
        device="Tablet"
    else:
        device='Others'

    return device
