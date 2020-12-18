
# import requests
#
# url = 'https://lanhuapp.com/web/#/item/project/board?pid=7c3320e7-e58c-40ef-a118-2f373a6513d1'
# r = requests.get(url)
# print(r.text)

def y():
    for i in range(2,10):
        yield i


r= y()
print(next(r))
print(next(r))
print(next(r))
print(next(r))