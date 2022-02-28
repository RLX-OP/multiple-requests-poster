# -- Import Packages -- #
import requests
import time
import pyfiglet
import json

# -- Setup -- #
print(pyfiglet.figlet_format('RLX \n REQUESTS \n POSTER'))
urlfile = open('config.json', mode = 'r')
url = json.load(urlfile)
proxyfile = open('proxies.txt', mode = 'r')

# -- Proxy, Url And Requests Setup Here -- #
for link in url:
  rlx = link['link']
  for content in proxyfile:
    proxy = { 'http': content }
    requests.get(rlx, headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62' }, proxies = proxy)
    print(time.strftime('==> (Day: %D, Hour: %H, Minute: %M, Second: %S) Request Sent Successfully.'))
	

# -- @INFO -- #
#   This Code Is Coded By RLX. 
#   Give Credit To Him.
# -- Also I Will Not Be Responsible For Anything You Do. -- #
