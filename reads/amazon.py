from amazon.api import AmazonAPI
import os
import urllib.request

amazon = AmazonAPI(os.environ['AMAZON_ACCESS_KEY'], os.environ['AMAZON_SECRET_KEY'], os.environ['AMAZON_ASSOC_TAG'])

class Amazon():

    def lookup(self, ItemId):
        print(amazon)
        print(amazon.aws_associate_tag)
        try:
            product = amazon.lookup(ItemId=ItemId)
            return product
        except urllib.error.HTTPError as e:
            print(e)
        except amazon.api.AsinNotFound as anf:
            print('AsinNotFound: ', anf)
        
        return None