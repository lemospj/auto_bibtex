from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from find_bibentry import bibtex_entry
import re
import bib_files

def auto_bib():
    url = 'https://mathscinet.ams.org/mathscinet'
    res = requests.get(url)
    mscinet = res.content
    soup = BeautifulSoup(mscinet, 'html.parser')

    bib_path = bib_files.find_bib_path()
    bib_build(url, soup, bib_path)

def more_entries(url, soup, path):
    more = input('\nDo you wish to add more entries? (Y/N)\n> ')
    if more.lower() == 'y':
        bib_build(url, soup, path)


def bib_build(url, soup, path):    
    author = input('\nAuthor: ')
    title = input('Title: ')

    req = {'s4' : author, 's5' : title, 'pg4' : 'AUCN', 'pg5' : 'TI'}

    form_info = soup.find('form', attrs = {'name' : 'pubsearch'}).attrs

    action = form_info['action']

    url_submit = urljoin(url, action)
    res_submit = requests.get(url_submit, params = req)

    submit_soup = BeautifulSoup(res_submit.content, 'html.parser')
    bib_entry = bibtex_entry(submit_soup, url_submit)

    if bib_entry != 0:                              # If bib_entry is 0, then no publications were found.
        bib_label = input('BibTex label: ')
        split_entry = re.split('({|,)', bib_entry)
        split_entry[2] = bib_label
        bib_entry = ''.join(split_entry)
        bib_files.create_bib(path, bib_entry)
    more_entries(url, soup, path)


if __name__ == '__main__':
    auto_bib()            