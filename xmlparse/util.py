import os
import datetime
from xmlparse.exceptions import ShortDateFormatException

LATEST = '1.0'

ANIMATION = """
    data-animation-name=fadeIn
    data-animation-duration=1000
    data-animation-delay=0
    """

def gFirst(l):
    return l[0]

def parse_link(textelem):
    #use dict or smth lol
    return (textelem.replace("!lb", "<a class=\"hyplink\"")
    .replace("!rb", ">")
    .replace("!cl", "</a>")
    .replace("!br", "<br>")
    .replace("!nb", "<a target=\"blank\" class=\"hyplink\"")
    .replace("!\\rb", "!rb")
    .replace("!\\nb", "!nb")
    .replace("!\\cl", "!cl"))

def get_path(file):
    return "skeletons/blocks/projprev/" + file

def get_proj_assetfile(file):
    f = os.path.basename(os.path.normpath(file))
    return "projassets/" + f + "/"

def parse_date(file, date): #mm/yyyy or mm/dd/yyyy
    split = date.split("/")
    if len(split) != 2 and len(split) != 3:
        raise ShortDateFormatException(file, date)

    valid = all([x for x in split if x.isnumeric()])
    if not valid:
        raise ShortDateFormatException(file, date)
    dt_mo = datetime.datetime.strptime(split[0], "%m")
    month = dt_mo.strftime("%B")
    year = split[1]
    if len(split) == 3:
        day = split[1]
        year = split[2]
        return month + " " + day + ", " + year
    return month + " " + year
