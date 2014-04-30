from flask_frozen import Freezer
from main import app, PAGES

freezer = Freezer(app)

@freezer.register_generator
def routing():
    for route in PAGES:
        yield {"route": route}

if __name__ == "__main__":
    freezer.run(debug=True)
