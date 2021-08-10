
def search_page1(tag):
    return tag.name == 'div' and tag.attrs = {'class' : 'pageTitle'}

def reply(soup):
    try:
        tag = soup.find_all(search_page1)[0]
        if 'No publications' in str(tag.get_text()):
            print('No publications were found.')
    except IndexError:
        try:
            
        except IndexError:
