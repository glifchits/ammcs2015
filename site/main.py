import os

from flask import Flask, render_template, abort, redirect
from config_pages import ROUTES, SESSIONS
app = Flask(__name__, template_folder="pages")

HTML = '.html'

@app.route('/')
def main():
    return render_template('index.html', pages=ROUTES)

@app.route('/home/')
@app.route('/index/')
def index():
    return redirect('/')

@app.route('/<string:route>/')
def root_routing(route):
    if route in ROUTES.values():
        template_name = route.strip() + HTML
        print 'rendering', template_name
        return render_template(template_name, pages=ROUTES, sessions=SESSIONS)
    else:
        abort(404)

@app.route('/special-sessions/<string:session>/')
def special_sessions(session):
    if session in SESSIONS.keys():
        template_name = 'special-sessions/' + session.strip() + HTML
        return render_template(template_name, pages=ROUTES, sessions=SESSIONS)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
