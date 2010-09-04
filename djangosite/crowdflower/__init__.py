import urllib, urllib2

from django.conf import settings

LOGIN_URL = 'https://crowdflower.com/login'

class CrowdFlowerHandler(urllib2.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

class CrowdFlower(object):
    def __init__(self, url, email):
        self.mob_url = url
        self.email = email
        self.opener = urllib2.build_opener(urllib2.HTTPSHandler, CrowdFlowerHandler())
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
            request = urllib2.Request(settings.CROWDFLOWER_URL)
            response = self.opener.open(request)
        except urllib2.HTTPError, auth_error:
            print 'First error (code %s)' % auth_error.code
            if auth_error.code != 401:
                raise auth_error
            if 'set-cookie' in auth_error.headers:
                cookie = auth_error.headers['set-cookie']
            else:
                raise Warning('The request returned with status 401, but did not set a cookie.')
            login_post = {
                '_method': 'put',
                'email': settings.CROWDFLOWER_EMAIL,
                'submit': 'Start Judging',
                }
            headers = {
                'Referer': settings.CROWDFLOWER_URL,
                'Cookie': cookie,
                }
            try:
                request = urllib2.Request(LOGIN_URL, urllib.urlencode(login_post.items()), headers)
                response = self.opener.open(request)
            except urllib2.HTTPError, redirect_error:
                print 'Second error (code %s)' % redirect_error.code
                if 300 <= redirect_error.code < 400:
                    if 'set-cookie' in redirect_error.headers:
                        cookie = redirect_error.headers['set-cookie']
                    headers = {
                        'Referer': settings.CROWDFLOWER_URL,
                        'Cookie': cookie,
                        }
                    request = urllib2.Request('https://crowdflower.com%s' % redirect_error.headers['location'], headers=headers)
                    try:
                        response = self.opener.open(request)
                        return response
                    except urllib2.HTTPError:
                        pass
            raise Exception('Unable to log in.')
    
    def fetch_one(self):
        if self.first_response:
            return self.first_response
        else:
            # TODO: Fetch another one
            return