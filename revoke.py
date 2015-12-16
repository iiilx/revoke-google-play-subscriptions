from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
from apiclient.discovery import build
from apiclient.errors import HttpError

PACKAGE_NAME = '<ANDROID PACKAGE NAME>'
SUBSCRIPTION_ID = '<SUBSCRIPTION ID / SKU>'
# 1 token on each line
TOKENS_FILE_PATH = '<PATH TO TOKENS FILE>'
EMAIL = '<GENERATED GOOGLE SERVICES ACCOUNT EMAIL>'
PRIVATE_KEY = '<GENERATED PRIVATE _KEY>'

class Client(object):
    SCOPE = 'https://www.googleapis.com/auth/androidpublisher'

    def __init__(self):
        credentials = SignedJwtAssertionCredentials(EMAIL, PRIVATE_KEY, self.SCOPE)
        http = Http()
        http = credentials.authorize(http)
        self.subscriptions = build('androidpublisher', 'v2', http=http).purchases().subscriptions()

    def revoke_subscription(self, package_name, token, sub_id):
        try:
            self.subscriptions.revoke(packageName=package_name,
                                             token=token,
                                             subscriptionId=sub_id).execute()
        except HttpError as e:
            if e.resp.status == 500:
                print 'got error %s when invalidating token' % e
            elif e.resp.status != 200:
                print 'got unexpected resp %s' % e

if __name__ == '__main__':
    c = Client()
    with open(TOKENS_FILE_PATH, 'r') as f:
        for token in f:
            c.revoke_subscription(PACKAGE_NAME, token, SUBSCRIPTION_ID)
