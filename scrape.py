#!/usr/bin/env python3
"""
http://archive.bridgesmathart.org/index.html
http://archive.bridgesmathart.org/2020/index.html
http://archive.bridgesmathart.org/2020/bridges2020-19.html
http://archive.bridgesmathart.org/2020/bridges2020-19.pdf

<a href="bridges2020-19.html"><div class="well well-sm">
			<span class="title">Adapter Tiles Evolves the Girih Tile Set</span><br/>
			<span class="authors">Lars Eriksson</span><br/>
			<span class="pages">Pages 19&ndash;26</span>
			</div></a>
"""

import json
from bs4 import BeautifulSoup
import requests


years = range(1998, 2021)
base_url = 'http://archive.bridgesmathart.org'


def main():
    data = scrape()

    with open('bridges-archive-data-by-year.json', 'w') as f:
        json.dump(data, f)


def scrape():

    data = {}
    for year in years:
        print(year)
        year_url = '%s/%d/index.html' % (base_url, year)

        resp = requests.get(year_url)
        soup = BeautifulSoup(resp.content, 'lxml')
        els = soup.findAll('a')

        prefix = 'bridges%d-' % year
        year_data = []
        for el in els:
            href = el.attrs['href']
            if not href.startswith(prefix):
                continue

            paper_data = {'year': year}

            for span in el.findAll('span'):
                if 'title' in span.attrs['class']:
                    paper_data['title'] = str(span.contents[0])
                if 'authors' in span.attrs['class']:
                    paper_data['authors'] = str(span.contents[0])

            paperid = href[len(prefix):-5]
            paper_data['id'] = paperid
            paper_data['html_link'] = '%s/%d/%s' % (base_url, year, href)
            paper_data['pdf_link'] = '%s/%d/%s' % (base_url, year, href.replace('html', 'pdf'))

            year_data.append(paper_data)
        print('  got %d papers' % len(year_data))

        data[year] = year_data

    return data


main()
