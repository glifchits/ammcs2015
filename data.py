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
    "bielecki": ('Tomasz', 'Bielecki', 'Illinois Institute of Technology', 'bielecki.jpg'),
    "zabaras": ('Nicholas', 'Zabaras', 'University of Warwick', 'zabaras.jpg'),
    "vanden-eijnden": ('Eric', 'Vanden-Eijnden', 'Courant Institute, New York University', 'vanden-eijnden.jpg'),
    "yi": ('Yingfei', 'Yi', 'University of Alberta', 'Yingfei-Yi.jpg'),
    "oosterlee": ('Kees', 'Oosterlee', 'Delft University of Technology and CWI', 'oosterlee.jpg'),
    "schreiber": ('Sebastian', 'Schreiber', 'University of California, Davis', 'schreiber.jpg'),
    "albert": (u'Réka', 'Albert', 'Pennsylvania State University', 'albert.png'),
    "liu": ('Wing Kam', 'Liu', 'Northwestern University', 'liu.jpg'),
    "mallat": (u'Stéphane', 'Mallat', 'Ecole Normale Superieure', 'mallat.jpg'),
    "fischer": ('Paul', 'Fischer', 'U of Illinois', 'fischer.png'),
    "abgrall": (u'Rémi', 'Abgrall', u'University of Zurich', 'abgrall.jpg')
}
semi_plenary = {
    "hurd": ('Tom', 'Hurd', 'McMaster University', 'hurd.jpg'),
    "kirr": ('Eduard-Wilhelm', 'Kirr', 'University of Illinois at Urbana-Champaign', 'kirr.jpg'),
    "zaccour": ('Georges', 'Zaccour', u'École des Hautes Études commerciales de Montréal', 'zaccour.jpg')
}

plenary_as_list = [ (key,) + plenary[key] for key in plenary.keys() ]
semi_plenary_as_list = [ (key,) + semi_plenary[key] for key in semi_plenary.keys() ]

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
        ('Jeanette', 'Haas', 'Administrative Support'),
        ('Michael', 'Murray', 'Electronic Publishing Coordinator'),
        ('Sanjay', 'Prabhakar', 'Computer Support'),
        ('Shyam', 'Badu', 'Digital Media Support'),
    )

    students = (
        ('Krishan', 'Rajaratnam', 'UW, Waterloo'),
        ('Igor', 'Ivashev', 'WLU, Waterloo'),
        ('Kenneth', 'Onuma', 'WLU, Waterloo'),
        ('Alexander', 'Howse', 'UW, Waterloo'),
        ('Alysha', 'Ahlin', 'WLU, Waterloo'),
        ('Amenda', 'Chow', 'UW, Waterloo'),
        ('Andrew', 'Harris', 'WLU, Waterloo'),
        ('Anisha', 'Mahant', 'WLU, Waterloo'),
        ('Asiya', 'Gul', 'WLU, Waterloo'),
        ('Januka', 'Shanmugarajah', 'WLU, Waterloo'),
        ('Katia', 'McDougall', 'WLU, Waterloo'),
        ('Lorena', 'Cid Montiel', 'UW, Waterloo'),
        ('Maryo', 'Ibrahim', 'WLU, Waterloo'),
        ('Mbika', 'Nfor', 'WLU, Waterloo'),
        ('Nilam', 'Lakhani', 'WLU, Waterloo'),
        ('Philip', 'McCarthy', 'UW, Waterloo'),
        ('Saqif', 'Abdullah', 'WLU, Waterloo'),
        ('Shada', 'Tabet', 'WLU, Waterloo'),
        ('Shazma', 'Ameen', 'WLU, Waterloo'),
        ('Syeda', 'Hussain', 'WLU, Waterloo'),
        ('Yuchen', 'Zhu', 'WLU, Waterloo'),
        ('Zaamilah', 'Balasubramaniam', 'WLU, Waterloo'),
        ('Zahra', 'Fotovatnia', 'WLU, Waterloo')
    )


