import requests
from pyquery import PyQuery


def getToken(session):
    url = 'https://nosec.org/home/index/threaten.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                      " like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    }
    requests.get
    html = session.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    doc = PyQuery(html.text)
    token = doc("[name=csrf-token]").attr("content")
    return token
