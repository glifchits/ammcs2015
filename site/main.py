from flask import Flask, render_template, abort, redirect
from config_pages import *
app = Flask(__name__)

HTML = '.html'

@app.route('/')
def main():
    print ROUTES.items()
    return render_template('index.html', pages=ROUTES)

@app.route('/home/')
@app.route('/index/')
def index():
    print 'routed to index'
    return redirect('/')

@app.route('/<string:route>/')
def routing(route):
    if route in ROUTES.values():
        template_name = route.strip() + HTML
        return render_template(template_name, pages=ROUTES)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
