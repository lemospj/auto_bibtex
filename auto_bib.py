from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = 'https://mathscinet.ams.org/mathscinet'
res = requests.get('https://mathscinet.ams.org/mathscinet')
mscinet = res.content
soup = BeautifulSoup(mscinet, 'html.parser')

author = input('Author: ')
title = input('Title: ')

req = {'s4' : author, 's5' : title, 'pg4' : 'AUCN', 'pg5' : 'TI'}

def right_form(tag):
    return tag.name == 'form' and tag['name'] == 'pubsearch'

form_info = soup.find_all(right_form)[0].attrs

action = form_info['action']
method = form_info.get('method', 'get')

if method == 'get':
    url_submit = urljoin(url, action)
    res_submit = requests.get(url_submit, params = req)
else:
    url_submit = urljoin(url, action)
    res_submit = requests.post(url_submit, data = req)

print(res_submit.url)