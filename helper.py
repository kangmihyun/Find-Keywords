from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urljoin, urlparse
from urllib.error import URLError, HTTPError
import re
def Extractlinks(url, locNet):
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

        if locNet not in link:
            # print("www.is.mcgill.ca", link)
            continue
        links.append(link)

    return links

def DFS(url ,visited , current_level, level_limit, locNet):
    visited.append(url)
    # print("URL: ", url)

    current_level += 1
    if(current_level == level_limit):
        return
    links = Extractlinks(url, locNet)
    # print("children links: ", links)
    for link in links:
        if link not in visited:
            DFS(link ,visited , current_level, level_limit, locNet)


def filter(links, keywords_pattern):
    filteredLinks = {}
    for link in links:
        keywordSet = set()
        req = Request(link)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        web_content = " ".join([repr(string) for string in soup.stripped_strings])
        # print(web_content)
        keywords_found = keywords_pattern.findall(web_content, re.IGNORECASE)
        if not keywords_found:
            continue
        for keyword in keywords_found:
            keywordSet.add(keyword)
        filteredLinks[link] = keywordSet
    return filteredLinks




if __name__ == '__main__':
    url = "http://www.is.mcgill.ca/studentaid/workstudy/postings/index.htm"
    #url = "http://www.is.mcgill.ca/studentaid/workstudy/postings/WS18060.htm"
    #Extractlinks("http://www.is.mcgill.ca/studentaid/workstudy/postings/index.htm")
    locNet = urlparse(url).netloc
    visited = []
    current_level = 0
    level_limit =  4
    sameDomain = True
    keywords = ["python"]
    keywords_pattern = re.compile('|'.join(keywords))
    DFS(url, visited, current_level, level_limit, locNet)
    print(visited)
    links = filter(visited, keywords_pattern)
    print(links)
