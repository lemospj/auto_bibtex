from bs4.element import Tag
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def author_tag(tag):                    
    if tag.name == 'a':
        return '/mathscinet/search/author.html' in tag['href']
    else:
        return False

def children_tags(tag):             # Given a tag, this function creates a list of all its children which are 
    l = []                          # also tags.
    for child in tag.children:
        if isinstance(child, Tag):
            l.append(child)
    return l

def many_pubs(soup):
    tag = soup.select('.row-body-border')[0]                    # A tag with class row-body-border only exists
    pub_list = []                                               # when there is more than one result. This can 
    i = 1                                                       # therefore be used to distinguish this case from
                                                                # the single result one.

    for child in children_tags(tag):                            # Build a list of publications.
        if 'headline' in child.attrs.get('class', [''])[0]:
            atag = child.a
            auttag = child.find_all(author_tag)                 # List of tags with info about the authors.
            tittag = child.select('.title')[0]
            pub_dict = {
                'index': i, 
                'authors' : [aut.get_text() for aut in auttag], 
                'title' : tittag.get_text(), 
                'link' : ''.join(['https://mathscinet.ams.org', atag['href']])
                }
            pub_list.append(pub_dict)
            i += 1
    
    for entry in pub_list:              # Menu of publications.
        print('{ind}. {aut}, {tit}'.format(
            ind = entry['index'], 
            aut = '; '.join(entry['authors']), 
            tit = entry['title'])
            )
    option = input('\nSelect a publication: ')
    
    try:
        new_url = pub_list[int(option) - 1]['link']
        new_res = requests.get(new_url)
        new_soup = BeautifulSoup(new_res.content, 'html.parser')
        return [new_soup, new_url]
    except IndexError: 
        return 0                    # Returns 0 if there are no publications.


def one_pub(soup, url):                             # Used to get to the page with the BibTex entry.
    tag_form = soup.find('form', attrs = {'class' : 'SelectDownloadFormat'})
    action = tag_form['action']
    s1_value = tag_form.find('input', attrs = {'name' : 's1'})['value']
    subm = {'fmt' : 'bibtex', 's1' : s1_value, 'pg1' : 'MR'}
    url_subm = urljoin(url, action)
    one_res = requests.get(url_subm, params = subm)
    one_soup = BeautifulSoup(one_res.content, 'html.parser')
    return one_soup


def get_bibtex(soup):
    tag = soup.pre
    return tag.get_text()


def bibtex_entry(soup, url):
    new_url = url
    new_soup = soup
    tag = soup.select('.pageTitle')[0]                  # Check whether there are no publications by looking at the
    if 'No publications' in tag.get_text():             # text in this tag.
        print('\nNo publications were found.')
        return 0
    else:
        try:                                            # If there are publications, try to run the routine many_pubs 
            mpubs = many_pubs(soup)
            new_url = mpubs[1]
            new_soup = mpubs[0]
        except IndexError:
            pass
        final_soup = one_pub(new_soup, new_url)
        return get_bibtex(final_soup)                                     
