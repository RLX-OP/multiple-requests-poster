# -- Import Packages -- #
import requests
import os
import time
import pyfiglet
import json

# -- Setup -- #
#pyfiglet('RLX \n REQUESTS \n POSTER')
urlfile = open('config.json', 'read')
url = json.load(urlfile)
proxyfile = open('proxies.txt', 'read')

# -- Proxy, Url And Requests Setup Here -- #
for link in url:
  rlx = link['link']
  for content in proxyfile:
    proxy = { 'http': content }
    requests.get(rlx, headers = { 'User-Agent':'Mozilla/5.0 (Linux; Android 10.0; RLX Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36 Edg/88.0.705.63' }, proxies = proxy)
    print(time.strftime('==> (Day: %D, Hours: %H, Minutes: %M, Seconds: %S) Request Sent Successfully.'))
	

# -- @INFO -- #
#   This Code Is Coded By RLX. 
#   Give Credit To Him.
# -- Also I Will Not Be Responsible For Anything You Do. -- #