# import re
import requests
import simplejson as json

def get_json(url):
    r = requests.get(url)
    return(json.loads(r.text))
