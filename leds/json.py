import requests
import simplejson as json

def get_json(url):
    """Get the json inton a dict"""
    r = requests.get(url)
    return(json.loads(r.text))
