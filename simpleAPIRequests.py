import requests
import os
from PIL import Image
from IPython.display import IFrame

url = 'https://www.imb.com/'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)