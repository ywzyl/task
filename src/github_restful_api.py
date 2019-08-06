#coding=utf-8
import requests

def github_restful_api():
    url = "https://developer.github.com/v3/users/#get-the-authenticated-user"
    response = requests.get(url=url)
    print(response.text)

github_restful_api()