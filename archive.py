#!/usr/bin/env python3
import json
import os
import re
import time
import urllib.request


archive_path = '/home/alan/Downloads/bridges-math-papers'

def main():
    with open('bridges-archive-data-by-year.json') as f:
        data = json.load(f)

    for year, year_data in data.items():
        print(year)
        pth = '%s/%s' % (archive_path, year)
        os.makedirs(pth, exist_ok=True)
        for paper in year_data:
            filename = '%s/bridges-%s-%s-%s.pdf' % (pth, year, paper['id'], slugify(paper['title']))
            get_binary_file(paper['pdf_link'], filename)
            time.sleep(5*60)
            print('  downloaded %s' % paper['pdf_link'])
            print('          as %s' % filename)


def slugify(s):
    s = s.lower()
    s = re.sub('[ _]', '-', s)
    s = re.sub('[^0-9a-z\-]', '', s)
    return s


def get_binary_file(url, filename):
    response = urllib.request.urlopen(url)
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()


main()
