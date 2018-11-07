import urllib.parse
import urllib.request

def Getter(url):
    try:
        print(url)
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        urlHeaders = {'User-Agent': user_agent}
        req = urllib.request.Request(url,headers=urlHeaders)
        with urllib.request.urlopen(req) as response:
            return response.read()
    except Exception:
        return None
    return None