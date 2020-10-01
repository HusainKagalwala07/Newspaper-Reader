import json
import requests
from newsapi import NewsApiClient
import pywin32_system32
import time
n=1
def readit(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
readit("Welcome to CS news")
time.sleep(2)
readit("This system will provide u 10 latest headlines\nNews reading will be started in 3 second")
time.sleep(3)
newsapi = NewsApiClient(api_key="86dfa85a37c148b68a65772801c4c672")
top_headlines = newsapi.get_top_headlines(sources='google-news-in')

json_hlines=json.dumps(top_headlines)


parsed1=json.loads(json_hlines)
articles=parsed1['articles']
for i in articles:
    item=json.dumps(i)
    parse_item=json.loads(item)
    description=json.dumps(parse_item)
    parsed_discription=json.loads(description)
    data=parsed_discription['description']

    readit(f"News {n} : {data}")
    n=n+1
