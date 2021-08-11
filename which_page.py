from bs4.element import Tag
from bs4 import BeautifulSoup
import requests

def author_tag(tag):
    if tag.name == 'a':
        return '/mathscinet/search/author.html' in tag['href']
    else:
        return False

def children_tags(tag):
    l = []
    for child in tag.children:
        if isinstance(child, Tag):
            l.append(child)
    return l

def many_pubs(soup):
    tag = soup.select('.row-body-border')[0]
    pub_list = []
    i = 1
    for child in children_tags(tag):
        if 'headline' in child.attrs.get('class', [''])[0]:
            atag = child.a
            auttag = child.find_all(author_tag)[0]
            tittag = child.select('.title')[0]
            pub_dict = {'index': i, 'author' : auttag.get_text(), 'title' : tittag.get_text(), 'link' : ''.join(['https://mathscinet.ams.org', atag['href']])}
            pub_list.append(pub_dict)
            i += 1
    for entry in pub_list:
        print('{ind}. {aut}, {tit}'.format(ind = entry['index'], aut = entry['author'], tit = entry['title']))
    option = input('\nWhat publication are you looking for? ')
    try:
        new_url = pub_list[int(option) - 1]['link']
        new_res = requests.get(new_url)
        new_soup = BeautifulSoup(new_res.content, 'html.parser')
        print(new_url)
        return new_soup
    except IndexError: 
        return 0

def reply(soup):
    new_soup = 0
    tag = soup.select('.pageTitle')[0]
    if 'No publications' in tag.get_text():
        print('\nNo publications were found.')
    else:
        new_soup = many_pubs(soup)
    return new_soup
