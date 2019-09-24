# import re
import requests
import simplejson as json

def get_json():
    r = requests.get("http://web/color.json")
    return(json.loads(r.text))
