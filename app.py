from flask import Flask, render_template, flash, redirect, url_for, session, request, make_response
from helper import *
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    url = "http://www.is.mcgill.ca/studentaid/workstudy/postings/index.htm"
    locNet = urlparse(url).netloc
    visited = []
    current_level = 0
    level_limit =  4
    sameDomain = True
    keywords = ["python"]
    keywords_pattern = re.compile('|'.join(keywords))
    DFS(url, visited, current_level, level_limit, locNet)
    # print(visited)
    links = filter(visited, keywords_pattern)
    print(links)
    return render_template('search.html', links=links, num=len(links))

if __name__ == '__main__':
   app.run(debug = True)
