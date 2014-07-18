PAGE_FOLDER = 'pages'

routes = (
    ('Home', ''),
    ('Special Sessions & Minisymposia', 'special-sessions'),
    ('Contributed Sessions', 'contributed-sessions'),
    ('Submit Abstracts', 'submit-abstracts'),
    ('Deadlines & Payment', 'deadlines-payment'),
    ('Plenary Speakers', 'plenary-speakers'),
    ('Student Prize & Support', 'student-prize-support'),
    ('Conference Program', 'conference-program'),
    ('Proceedings', 'proceedings'),
    ('Conference Flyer', 'conference-flyer'),
    ('Travel & Local Info', 'travel-local-info'),
    ('Venue & Accommodation', 'venue-accommodation'),
    ('Organization', 'organization'),
    ('Contact Us', 'contact-us')
)

sessions = (
    ('scna',
    'The 2nd Canadian Symposium on Scientific Computing and Numerical Analysis',
    'TBA'),
    ('im', 'Industrial Mathematics', 'TBA'),
    ('mb', 'Mathematical Biology', 'TBA'),
    ('aads', 'Applied analysis and dynamical systems', 'TBA'),
    ('acm', 'Applied and computational mechanics', 'TBA'),
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

SESSIONS = {}
for code, title, orgs in sessions:
    SESSIONS[code] = (title, orgs)
