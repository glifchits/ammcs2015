PAGE_FOLDER = 'pages'

routes = (
    ('Home', 'index'),
    ('Special Sessions', 'special-sessions'),
    ('Contributed Sessions', 'contributed-sessions'),
    ('Submit Abstracts', 'submit-abstracts'),
    ('Deadlines & Payment', 'deadlines-payment'),
    ('Plenary Speakers', 'plenary-speakers'),
    ('Student Prize & Support', 'student-prize-support'),
    ('Travel Grants & Prizes', 'scholarships-grants-prizes'),
    ('Program', 'conference-program'),
    ('Proceedings', 'proceedings'),
    ('Conference Flyer', 'conference-flyer'),
    ('Travel & Local Info', 'travel-local-info'),
    ('Venue & Accommodation', 'venue-accommodation'),
    ('Organization & History', 'organization-history'),
    ('Contact Us', 'contact-us')
)

sessions = (
    ('sgt', 'Structured Graph Theory', 'Chinh Hoang and Kathie Cameron (WLU)'),
    ('me', 'Mathematical Epidemiology', 'Connel McCluskey'),
)

# determines the set of accessible pages
import os
PAGES = set()
for root, directory, files in os.walk(PAGE_FOLDER):
    for page in files:
        if page.startswith('_'): continue
        fullpath = os.path.join(root, page)[len(PAGE_FOLDER)+1:]
        namedpath = os.path.splitext(fullpath)[0]
        PAGES.add(namedpath)

# exports the ROUTES OrderedDict
from collections import OrderedDict
ROUTES = OrderedDict()
for k, v in routes:
    ROUTES[k] = v

SESSIONS = OrderedDict()
for code, title, orgs in sessions:
    SESSIONS[code] = (title, orgs)
