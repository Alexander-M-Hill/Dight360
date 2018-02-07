# Alexander Hill
# This made my cry on the outside and inside
# BRIEF SUMMARY:
# For the task of scraping the site and all of the associate links I first defined the two required functions.
# I then used a while loop to keep working through all of the different links and used a nested while loop to check for duplicates and throw out repeats.

import re
import requests as r
import time
import random
from bs4 import BeautifulSoup

reg_ends=re.compile("scrape/(.*?)$")
url_rnlp = 'http://reynoldsnlp.com/scrape/'
headers = {'user-agent': 'Alexander Hill (lex.m.hill@gmail.com)'}

def get_rnlp(extension):
    response = r.get(url_rnlp + extension, headers=headers)
    time.sleep(random.uniform(1.5, 2.5))
    with open('scrape/' + extension, 'w') as out_file:
        print(response.text, file=out_file)

def get_hrefs(filename):
    with open('scrape/' + filename) as html_file:
        soup = BeautifulSoup(html_file, 'html5lib')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            links.append(href)
        return links

to_do = ['aa.html']

already_scraped = []

while (to_do != []):
    
    for each in to_do:
        get_rnlp(each)
    
    for each in to_do:
        list_links = get_hrefs(each)
        set(list_links)
        new_endings = ([m.group(1) for l in list_links for m in [reg_ends.search(l)] if m])
        num_new = len(new_endings)

    num_todo = len(to_do)

    for x in range(num_todo):
        already_scraped.append(to_do.pop(0))

    while (new_endings != []):
        if new_endings[0] in already_scraped:
            new_endings.pop(0)
        else:
            to_do.append(new_endings.pop(0))
