from flask_frozen import Freezer
from main import app, PAGES
import shutil
os = shutil.os

freezer = Freezer(app)

@freezer.register_generator
def routing():
    for route in PAGES:
        yield {"route": route}

if __name__ == "__main__":
    if os.path.exists('build'):
        shutil.rmtree('build')
    freezer.freeze()
    oldcwd = os.getcwd()
    os.chdir('build')
    import SimpleHTTPServer, SocketServer
    PORT = 8000
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    try:
        print "serving at port", PORT
        httpd.serve_forever()
    except KeyboardInterrupt:
        print 'caught KeyboardInterrupt'
        raise
    finally:
        print 'shutting down'
        httpd.shutdown()
        os.chdir(oldcwd)
