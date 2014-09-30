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


sessions = [
    ('ddd', 'ss', 'Title: TBA', (
            'Elena Braverman (University of Calgary)',
            'Anatoli Ivanov (Penn State University)'
        )
    ),
    ('hs', 'ss', 'Title: TBA', (
            'Xinzhi Liu (University of Waterloo)',
        )
    ),
    ('msmb', 'ss', 'Modeling & Simulation in Medicine and Biology', (
            'Suzanne Shontz (University of Kansas)',
            'Corina Drapaca (Penn State University)'
        )
    ),
    ('mmnn', 'ss', 'Mathematical Models for Nanoscience and Nanotechnology',
        ( 'Zoran Miskovic and Hamed Majedi (University of Waterloo)',)
    ),
    ('aaip', 'ss', 'Title TBA',
        ( 'Herb Kunze (University of Guelph)', )
    ),
    ('sndta', 'ss', 'Title TBA',
        ( 'Manuele Santoprete (WLU, Waterloo)', )
    ),
    ('scna', 'st', 'The 2nd Canadian Symposium on Scientific Computing and Numerical Analysis', (
            'Scott MacLachlan (MUN)',
            'Justin Wan (Waterloo)',
            'Hans de Sterck (Waterloo)',
            'Ben Adcock (SFU)'
        )
    ),
    ('im', 'st', 'Industrial Mathematics', (
            'Huaxiong Huang (York)',
            'John Stockie (SFU)',
            'Odile Marcotte (UQAM & CRM)',
            'Sean Bohun (UOIT)',
        )
    ),
    ('mb', 'st', 'Mathematical Biology', (
            'Frithjof Lutscher (Ottawa)',
            'Lea Popovic (Concordia)'
        )
    ),
    ('aads', 'st', 'Applied analysis and dynamical systems', (
            'Xingfu Zou (UWO)',
            'Dmitry Pelinovsky (McMaster)',
            'David Iron (Dalhousie)'
        )
    ),
    ('acm', 'st', 'Applied and computational mechanics', (
            'Marek Stasna (Waterloo)',
            'Bartek Protas (McMaster)'
        )
    ),
]

sessions.sort(key = lambda sess: sess[0]) # sort by code
sessions.sort(key = lambda sess: sess[1]) # sort by type (SS, ST)

sess_by_code = \
    { code: (info, org, stype)
        for code, stype, info, org in sessions }

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
        ('Sanjay', 'Prabhakar', 'Computer Support'),
        ('Shyam', 'Badu', 'Digital Media Support'),
    )

    students = (
        ('Igor', 'Ivashev', 'WLU, Waterloo'),
        ('Kenneth', 'Onuma', 'WLU, Waterloo')
    )


