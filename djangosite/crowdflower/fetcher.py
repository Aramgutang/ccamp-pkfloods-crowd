import urllib, urllib2, cookielib

from django.conf import settings

LOGIN_URL = 'https://crowdflower.com/login'

class CrowdFlowerHandler(urllib2.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

class CrowdFlowerFetcher(object):
    def __init__(self, url, email):
        self.mob_url = url
        self.email = email
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPSHandler, urllib2.HTTPCookieProcessor(self.cookies), CrowdFlowerHandler())
        self.opener.addheaders = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Accept-Encoding': '',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Keep-Alive': '115',
            'Connection': 'keep-alive',
            }.items()
        self.first_response = self.log_in()
    
    def log_in(self):
        try:
            request = urllib2.Request(self.mob_url)
            response = self.opener.open(request)
        except urllib2.HTTPError, auth_error:
            print 'First error (code %s)' % auth_error.code
            if auth_error.code != 401:
                raise auth_error
            login_post = {
                '_method': 'put',
                'email': self.email,
                'submit': 'Start Judging',
                }
            try:
                request = urllib2.Request(LOGIN_URL, urllib.urlencode(login_post.items()))
                request.add_header('Referer', self.mob_url)
                response = self.opener.open(request)
            except urllib2.HTTPError, redirect_error:
                print 'Second error (code %s)' % redirect_error.code
                if 300 <= redirect_error.code < 400 and 'location' in redirect_error.headers:
                    self.url = 'https://crowdflower.com%s' % redirect_error.headers['location']
                    request = urllib2.Request(self.url)
                    request.add_header('Referer', settings.CROWDFLOWER_URL)
                    try:
                        return self.opener.open(request)
                    except urllib2.HTTPError:
                        pass
            raise Exception('Unable to log in.')
    
    def fetch_one(self):
        if 'first_response' in self.__dict__:
            return self.__dict__.pop('first_response')
        else:
            tries = 0
            while tries < 3:
                try:
                    request = urllib2.Request(self.url)
                    request.add_header('Referer', self.url)
                    return self.opener.open(request)
                except urllib2.HTTPError, err:
                    tries += 1
                    raise Warning('Got a %s response. Retrying...' % err.code)