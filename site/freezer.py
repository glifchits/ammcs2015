from flask_frozen import Freezer
from main import app, ROUTES, SESSIONS

freezer = Freezer(app)

@freezer.register_generator
def root_routing():
    for route in ROUTES.itervalues():
        yield {"route": route}

@freezer.register_generator
def special_sessions():
    for session in SESSIONS.keys():
        yield {"session": session}

if __name__ == "__main__":
    freezer.run(debug=True)
