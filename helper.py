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
        if not link:
            continue
        # dealong with relative paths
        if("http:" not in link ):
            link = urljoin(url, link)
        links.append(link)

    return links

def DFS(url ,visited , current_level, level_limit):
    visited.append(url)
    print("URL: ", url)

    current_level += 1
    if(current_level == level_limit):
        return
    links = Extractlinks(url)
    print("children links: ", links)
    for link in links:
        if link not in visited:
            DFS(link ,visited , current_level, level_limit)



if __name__ == '__main__':
    url = "http://www.is.mcgill.ca/studentaid/workstudy/postings/index.htm"
    # url = "http://www.mcgill.ca/studentaid/work-study/students/next-steps#hired"
    Extractlinks( "http://www.is.mcgill.ca/studentaid/workstudy/postings/index.htm")
    visited = []
    current_level = 0
    level_limit =  3
    DFS(url, visited, current_level, level_limit)
    print(visited)
