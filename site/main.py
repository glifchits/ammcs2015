# -*- coding: utf-8 -*-

# builtin
import os
from collections import OrderedDict
# library
from flask import Flask, render_template, abort, redirect
from data import routes, sessions
# modules
import data

HTML = '.html'
PAGE_FOLDER = 'pages'

app = Flask(__name__, template_folder=PAGE_FOLDER)


@app.template_filter('natural_list')
def natural_list(lst):
    def to_str(e):
        return e.decode('utf-8')
    lst = map(to_str, lst)
    return ', '.join(lst)

# determines the set of accessible pages
PAGES = set()
for root, directory, files in os.walk(PAGE_FOLDER):
    for page in files:
        if page.startswith('_'): continue
        fullpath = os.path.join(root, page)[len(PAGE_FOLDER)+1:]
        namedpath = os.path.splitext(fullpath)[0]
        PAGES.add(namedpath)

def data_obj():
    '''Get a dictionary of all attributes in the `data` module'''
    keys = [ k for k in dir(data) if not k.startswith('_') ]
    return { k: eval('data.'+k) for k in keys }


@app.route('/')
def main():
    return render_template('index.html', pages=ROUTES)


@app.route('/<path:route>')
@app.route('/<path:route>/')
def routing(route):
    if route in PAGES:
        obj = data_obj()
        ROUTES = OrderedDict()
        for k, v in routes:
            ROUTES[k] = v
        return render_template(route+HTML, pages=ROUTES, **obj)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
