from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from which_page import bibtex_entry
import glob
import os
import re


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


submit_soup = BeautifulSoup(res_submit.content, 'html.parser')
bib_entry = bibtex_entry(submit_soup, url_submit)

bib_label = input('BibTex label: ')
split_entry = re.split('({|,)', bib_entry)
split_entry[2] = bib_label
bib_entry = ''.join(split_entry)


########## CREATE .BIB FILE #############
if bib_entry != 0:
    cwd = os.getcwd()
    print('Current directory: {cwd}'.format(cwd = cwd))
    cur_dir = input('\nUse current directory? (Y/N)\n> ')

    if cur_dir.lower() == 'y':
        target_path = cwd
    elif cur_dir.lower() == 'n':
        target_path = input('\nWhat is the directory where you want the .bib file to be?\n> ')

    bib_path = os.path.join(target_path, '*.bib')
    bib_list = glob.glob(bib_path)

    bib_file = 0

    while bib_file == 0:
        if len(bib_list) == 1:
            use_bib = input('Use {bibf}?\n> '.format(bibf = bib_list[0]))
            if use_bib.lower() == 'y':
                bib_file = bib_list[0]
            else:
                bib_list.pop()
        else:
            bib_file = input('\nFile name: ')
            if bib_file[-4:] != '.bib':
                bib_file = ''.join([bib_file, '.bib'])
            bib_file = os.path.join(target_path, bib_file)

    with open(bib_file, 'a') as bib_write:
        bib_write.write(bib_entry)