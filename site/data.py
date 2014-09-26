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

sessions = (
    ('scna',
        'The 2nd Canadian Symposium on Scientific Computing and Numerical Analysis',
        (
            'Scott MacLachlan (MUN)', 'Justin Wan (Waterloo)',
            'Hans de Sterck (Waterloo)',
            'Ben Adcock (SFU)'
        )
        )
    ,
    ('im',
        'Industrial Mathematics',
        (
            'Huaxiong Huang (York)',
            'John Stockie (SFU)',
            'Odile Marcotte (UQAM & CRM)',
            'Sean Bohun (UOIT)',
        )
        )
    ,
    ('mb',
        'Mathematical Biology',
        (
            'Frithjof Lutscher (Ottawa)',
            'Lea Popovic (Concordia)'
        )
        )
    ,
    ('aads', 'Applied analysis and dynamical systems',
        (
            'Xingfu Zou (UWO)',
            'Dmitry Pelinovsky (McMaster)',
            'David Iron (Dalhousie)'
        )
        )
    ,
    ('acm', 'Applied and computational mechanics',
        ('Marek Stasna (Waterloo)', 'Bartek Protas (McMaster)')
        )
    ,
)

sess_by_code = { code: (info, org) for code, info, org in sessions }

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
    )

    general_chairs = (
        ('Jacques', 'Bélair', 'University of Montreal'),
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
        ('Sanjay', 'Prabhakar', 'Computer Support'),
        ('Shyam', 'Badu', 'Digital Media Support'),
    )

    students = (
        ('Igor', 'Ivashev', 'WLU, Waterloo'),
        ('Kenneth', 'Onuma', 'WLU, Waterloo')
    )


