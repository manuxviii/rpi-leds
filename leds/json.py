import re
import requests

def get_color():
    r = requests.get("localhost/color.json")
    str = re.sub("\"", r':', r.text)
    return(str.split(":")[4])
