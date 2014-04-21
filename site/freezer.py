from flask_frozen import Freezer
from main import app, ROUTES

freezer = Freezer(app)

@freezer.register_generator
def routing():
    for route in ROUTES.itervalues():
        yield {"route": route}

if __name__ == "__main__":
    freezer.run(debug=True)
