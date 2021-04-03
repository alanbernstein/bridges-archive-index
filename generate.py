#!/usr/bin/env python3
import jinja2
import json


TEMPLATE_FILE = "bridges-archive-index-template.html"
output_file = 'bridges-archive-index.html'


def main():
    with open('bridges-archive-data-by-year.json') as f:
        data = json.load(f)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(TEMPLATE_FILE)
    rendered = template.render(data=data)

    with open(output_file, 'w') as f:
        f.write(rendered)

    print('wrote %d bytes to %s' % (len(rendered), output_file))


main()
