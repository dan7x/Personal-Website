from xmlparse.util import parse_link, ANIMATION, parse_date

def create(elem, filename):
    parsed_text = parse_link(str(elem.text))
    title_data = {
        'title_text': parsed_text,
        'isMain': elem.tag == "title",
        'anim': ANIMATION,
        'author' :None,
        'date': None
        }
    if elem.tag == "title":
        if 'author' in elem.attrib:
            title_data["author"] = elem.attrib["author"]
        if 'date' in elem.attrib:
            title_data["date"] = elem.attrib["date"]
        if 'shortdate' in elem.attrib:
            title_data["date"] = parse_date(filename, elem.attrib["shortdate"])
    return title_data