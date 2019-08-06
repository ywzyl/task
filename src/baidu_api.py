#coding=utf-8
import requests

def baidu_open_api():
    url = "http://api.map.baidu.com/place/v2/search"
    params = {
        'query':'ATM机',
        'tag':'银行',
        'region':'北京',
        'output':'json',
        'ak':'34GjQhOdtBVigAn6Vxt14TO8VdP7XwiE'
    }

    response = requests.get(url=url, params=params)
    print(response.text)

baidu_open_api()




