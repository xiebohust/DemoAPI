
import json
import requests
import pymysql

requests.session()

def send_request(method='POST',url=None,params=None,data=None,verify=False):
    return requests.request(method=method,url=url,params=params,data=data,verify=verify)

def register():
    url = 'https://api.shiqichuban.com/v1/user/register'
    data = {
        "password": "test123",
        "mobile": "12345678906",
        "nickname": "",
        "type": "1",
        "captcha": "shiqi"
    }


    r = requests.post(url=url,data=data,verify=False)
    print(type(r))
    d = r.json()
    print(d)

# register()

def login():
    url = 'https://www.shiqichuban.com/user/login_popup'
    data = {
	"mobile": "12345678906",
	"password": "test123"
    }
    method = 'POST'
    s = requests.Session()
    r = s.request(method=method,url=url,data=data,verify=False)
    # print(r.json())
    cookies = r.cookies.get_dict()
    print(r.json())
    return cookies



def article_list():
    url = 'https://api.shiqichuban.com/v2/article/list'
    data = {
	"offset": 10,
	"default": 1
    }
    method = 'POST'
    r = requests.request(method=method,url=url,data=data,verify=False)
    print(r.json())
    print(r.json()['articles'])

def logout():
    url = 'https://api.shiqichuban.com/v1/user/logout'
    method = 'GET'
    # r = send_request(method=method,url=url)
    s = login()
    r = s.request(method=method,url=url,verify=False)
    print(r.json())


def user_items():
    url = 'https://api.shiqichuban.com/v2/user/items'
    data = {
	"type": 1,
	"next_start": "",
	"amount": 20
}

    # r = login().request('POST',url,verify=False)
    r = requests.request('POST',url,data=data,cookies=login(),verify=False)

    print(r.json())


def book_list():
    url = 'https://api.shiqichuban.com/v1/book/list'
    data = {"type":0,
            "theme_list":[1,2,3,4,5,7],
            "count":20,
            "next_start":None}

    method = 'POST'
    headers = {'Content-Type':'application/json'}
    cookies = {'XSRF-TOKEN': 'eyJpdiI6IjBPMmx1TkRSMGoxakE3dTl4ZWJYcGc9PSIsInZhbHVlIjoidGZUXC9iM2hsREEzNU5RM0JxZFRDajhLdE1zalJMaWNicWU1b2doR1RmVjR1RW05ejRDUHJyeHhPdkR3OUpOaHhXNWpxZlhQMkVDOG5IY3Y1cmxFYkV3PT0iLCJtYWMiOiJlOWIxMGNkY2EwMDIxNzkyM2NlZTNhYWYzZjY1YjZkNmRjMGZlYzg2MzQ3NGQ4MmFhZTY1MmY2YjMxZGU1N2U1In0%3D', 'laravel_session': 'eyJpdiI6IjlkSFlzSHRjb09yZWxudUJyaXFBMEE9PSIsInZhbHVlIjoidStMMXY1c0U5Q3JHeU03cm1qcmJGRUtSU3J5b0pLWithUE9vVFI0TGlsU0tiTE0xOU8ySEw0ZXFqWlNFV1Arek5DM3pDWFM1N2d2S2hoRWpMNFY1TFE9PSIsIm1hYyI6IjhmMTYzZjcyNmFkM2I4OWVjNWFjOTQzN2U4ZmVhNmZkODljZGFmZWNlMzFiNGNlYjI4NGQyM2EwNmRlNzJkM2MifQ%3D%3D'}
    r = requests.request(method,url,cookies=cookies,verify=False,headers=headers)
    print(r)
    if r:
        print(r.json())
        print(r.text)

if __name__ == '__main__':
    # login()
    book_list()
# user_items()