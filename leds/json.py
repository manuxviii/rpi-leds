# import re
import requests
import simplejson as json

def get_json(field="favcolor"):
    r = requests.get("http://web/color.json")
    ret = json.loads(r.text)
    return(ret[field])
