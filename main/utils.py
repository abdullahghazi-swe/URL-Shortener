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