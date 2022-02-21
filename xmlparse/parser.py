import xml.etree.ElementTree as ET
from flask import render_template
from xmlparse.util import get_path, LATEST
from xmlparse.projectgen import titles, text, media, carousel, block
from xmlparse.exceptions import UndefinedElementException

def generate(filename): #both the xml file name and the asset folder name
    tree = ET.parse(filename + ".xml")
    root = tree.getroot()
    generated = ""
    VERSION = LATEST
    if 'version' in root.attrib:
        VERSION = root.attrib['version']
        #run errorcheck?
    if root.tag == "project":
        html_out = ""
        for child in root:
            generated += generate_project_element(child, filename) + "\n"

    elif root.tag == "course":
        pass #to implement
    else:
        pass #error
    return generated

def generate_project_element(elem, filename):
    tag = elem.tag
    if tag == "title" or tag == "subtitle":
        TITLE_PATH = get_path("title.html")
        return render_template(TITLE_PATH, **titles.create(elem, filename))
    elif tag == "text":
        TEXT_PATH = get_path("text.html")
        return render_template(TEXT_PATH, **text.create(elem, filename))
    elif tag == "img" or tag == "vid":
        MEDIA_PATH = get_path("media.html")
        return render_template(MEDIA_PATH, **media.create(elem, filename))
    elif tag == "block":
        BLOCK_PATH = get_path("paragraphs.html")
        return render_template(BLOCK_PATH, **block.create(elem, filename))
    elif tag == "carousel":
        CAROUSEL_PATH = get_path("carousel.html")
        return render_template(CAROUSEL_PATH, **carousel.create(elem, filename))
    elif tag == "meta":
        return ""

    raise UndefinedElementException(filename, elem)