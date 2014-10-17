#-*- coding: utf-8 -*-

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

from special_sessions import sessions

sessions.sort(key = lambda sess: sess[0]) # sort by code
sessions.sort(key = lambda sess: sess[1]) # sort by type (SS, ST)

sess_by_code = \
    { code: (info, org, stype)
        for code, stype, info, org in sessions }

plenary = {
    "budd": ('Chris', 'Budd', 'University of Bath', 'budd.jpg'),
    "zabaras": ('Nicholas', 'Zabaras', 'University of Warwick', 'zabaras.jpg'),
    "vanden-eijnden": ('Eric', 'Vanden-Eijnden', 'Courant Institute, New York University', 'vanden-eijnden.jpg'),
    "yi": ('Yingfei', 'Yi', 'University of Alberta', 'Yingfei-Yi.jpg'),
    "oosterlee": ('Kees', 'Oosterlee', 'Delft University of Technology and CWI', 'oosterlee.jpg'),
    "schreiber": ('Sebastian', 'Schreiber', 'University of California, Davis', 'schreiber.jpg')
}

plenary_as_list = [ (key,) + plenary[key] for key in plenary.keys() ]

abstracts_link = 'https://www.conference-service.com/ammcs15/welcome.cgi'
registration_link = 'https://events.mylaurier.ca/current.htm?action=registerStart&eventId=58'

class committee:
    scientific = (
        ('Carlos', 'Garcia-Cevera', 'University of California, Santa Barbara'),
        ('David', 'Cai', 'New York University'),
        ('Dimitri', 'Vvedensky', 'Imperial College London'),
        ('John', 'Lowengrub', 'University of California, Irvine'),
        ('Nicholas', 'Zabaras', 'University of Warwick'),
        ('Shaofan', 'Li', 'University of California, Berkeley'),
        ('Chi-Wang', 'Shu', 'Brown University'),
        ('Boris', 'Malomed', 'Tel Aviv University'),
        ('Anatoli', 'Ivanov', 'Penn State University'),
        ('Olof', 'Runborg', 'KTH Royal Institute of Technology'),
        ('Alberto', 'Bressan', 'Penn State University'),
        ('Konstantina', 'Trivisa', 'University of Maryland'),
        ('Ronald', 'Coifman*', 'Yale University'),
        ('Andrew', 'Majda*', 'New York University'),
        ('Maciej', 'Zworski*', 'University of California, Berkeley'),
    )

    general_chairs = (
        ('Jacques', u'Bélair', 'University of Montreal'),
        ('Roman', 'Makarov', 'Wilfrid Laurier University, Waterloo'),
        ('Roderick', 'Melnik', 'Wilfrid Laurier University, Waterloo')
    )

    organizing = (
        ('Herb', 'Kunze', 'Congress Program Chair, University of Guelph'),
        ('Zilin', 'Wang', 'Congress Treasurer, WLU, Waterloo'),
        ('Chester', 'Weatherby', 'Student Prize Committee Chair, WLU, Waterloo'),
        ('Ian', 'Frigaard', 'Global OC, University of British Columbia, Vancouver'),
        ('Raymond', 'Spiteri', 'Global OC, University of Saskatchewan, Saskatoon'),
    )

    technical = (
        ('Michael', 'Murray', 'Electronic Publishing Coordinator'),
        ('Sanjay', 'Prabhakar', 'Computer Support'),
        ('Shyam', 'Badu', 'Digital Media Support'),
    )

    students = (
        ('Igor', 'Ivashev', 'WLU, Waterloo'),
        ('Kenneth', 'Onuma', 'WLU, Waterloo')
    )


