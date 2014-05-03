import os

from flask import Flask, render_template, abort, redirect
from config_pages import PAGE_FOLDER, PAGES, ROUTES, SESSIONS

app = Flask(__name__, template_folder=PAGE_FOLDER)

HTML = '.html'

@app.route('/')
def main():
    return render_template('index.html', pages=ROUTES)

@app.route('/<path:route>')
@app.route('/<path:route>/')
def routing(route):
    if route in PAGES:
        return render_template(route+HTML,
            pages = ROUTES,
            sessions = SESSIONS
        )
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
