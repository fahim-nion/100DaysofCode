import requests
#if a verification of human or not comes then
# import time
# from fake_useragent import UserAgent


url = "https://fojik.site/movie/agent-kim-reactivated/"

# session = requests.Session()

# headers = 
r = requests.get(url)

with open ("file.html" , "w" ,encoding="utf-8") as f:
    f.write(r.text)