import re
import requests
import httpauth


def get_color():
    r = requests.get(httpauth.url, auth=(httpauth.login, httpauth.passwd))
    str = re.sub("\"", r':', r.text)
    return(str.split(":")[4])
