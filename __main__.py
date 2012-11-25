import bitdeli
from bitdeli.widgets import Title, Description, Line, Text, set_theme
from datetime import datetime, timedelta
import random

set_theme('bluered')

random.seed(1)

def month():
    first = datetime.today()
    for i in range(30):
        yield (first + timedelta(days=i)).isoformat()

def data_exp():
    for i, date in enumerate(month()):
         yield date, (2**(i * 0.2) + random.gauss(10, 2)) * 1000

def data_lin():
    for i, date in enumerate(month()):
        yield date, (i + random.gauss(10, 2)) * 1000

for profile in bitdeli.profiles():
    pass

Line(size=(10, 7),
     data=[{'label': 'Android users', 'data': list(data_exp())},
           {'label': 'IPhone users', 'data': list(data_exp())},
           {'label': 'Web users', 'data': list(data_lin())}])

Text(head="98%", size=(2, 2))
Text(head="87%", size=(2, 2), color=2)
Text(head="22%", size=(2, 2), color=3)

Title("Week-to-week growth for Android is 98%")
Description("**86%** of users have been active in the past week. Latest version has been downloaded **2,347** times since October 24th.")