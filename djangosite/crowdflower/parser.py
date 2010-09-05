import re
from BeautifulSoup import BeautifulSoup

smsrx = re.compile(r'<h3>The SMS:\s*\[\s*(?P<sms>.+?)\s*\]\s*</h3>$')
uidrx = re.compile(r'^(?P<uid>\w+)\[.*\]$')

class CrowdFlowerParser(object):
    def __init__(self, page):
        self.soup = BeautifulSoup(page)
        match = smsrx.match(unicode((self.soup('h3') or ['',])[0]))
        if not match:
            raise Exception('No SMS found on page.')
        self.sms = match.groups('sms')[0]
        for input in self.soup('input'):
            if input.get('name', ''):
                match = uidrx.match(input['name'])
                if match:
                    self.uid = match.groups('uid')[0]
        if not hasattr(self, 'uid'):
            raise Exception('The UID of the SMS could not be identified.')