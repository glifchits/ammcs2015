routes = (
    ('Home', 'index'),
    ('Special Sessions', 'special-sessions'),
    ('Contributed Sessions', 'contributed-sessions'),
    ('Submit Abstract', 'submit-abstract'),
    ('Deadlines & Payment', 'deadlines-payment'),
    ('Plenary Speakers', 'plenary-speakers'),
    ('Student Prize & Support', 'student-prize-support'),
    ('Program', 'conference-program'),
    ('Proceedings', 'proceedings'),
    ('Conference Flyer', 'conference-flyer'),
    ('Travel & Local Info', 'travel-local-info'),
    ('Venue & Accommodation', 'venue-accommodation'),
    ('Organization & History', 'organization-history'),
    ('Contact Us', 'contact-us')
)

# exports the ROUTES OrderedDict
from collections import OrderedDict
ROUTES = OrderedDict()
for k, v in routes:
    ROUTES[k] = v