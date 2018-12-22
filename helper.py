from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError
import re
def Extractlinks(url):
    links = []
    req = Request(url)
    try:
        html_page = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
        return links
    except URLError as e:
        print('Reason: ', e.reason)
        return links
    except:
        print('unknown error')
        return links
    soup = BeautifulSoup(html_page, "lxml")

    for linkTag in soup.findAll('a'):
        link = linkTag.get('href')
        # dealong with relative paths
        if("http:" not in link ):
            link = urljoin(url, link)
        links.append(link)

    return links

if __name__ == '__main__':
    Extractlinks( "http://www.is.mcgill.ca/studentaid/workstudy/postings/index.htm")
