from flask import render_template
import xml.etree.ElementTree as ET
import os
from xmlparse.exceptions import (MissingElementException,
MetaNotFoundException,BadAttributeValueException,
DuplicateElementException, UndefinedElementException)

def generate_project_list(proj_root):
    ITEM_FILE = "skeletons/blocks/project_item.html"
    generated = []
    for filename in os.listdir(proj_root):
        f = os.path.join(proj_root, filename)
        metadata = []
        if os.path.isfile(f): # if file, not rlly needed
            root = ET.parse(f).getroot()
            for c in root:
                if c.tag == 'meta':
                    metadata.append(c)
            if len(metadata) != 1:
                raise MetaNotFoundException(proj_root)
            metadata=metadata[0]
        else:
            continue
        data = {
            'filename' : os.path.splitext(filename)[0],
            'assetpath' : os.path.join("projassets/", os.path.splitext(filename)[0] + "/")
        }
        rank = -1
        for ch in metadata:
            if ch.tag in data:
                raise DuplicateElementException(filename, "<meta>", ch.tag)
            if ch.tag == 'title' or ch.tag == 'desc' or ch.tag == 'thumb':
                data[ch.tag] = ch.text
            elif ch.tag == 'rank':
                try:
                    if not ch.text.isnumeric():
                        raise BadAttributeValueException(filename, "<rank>", '(val)', "(positive num)", "non-numeric")
                except AttributeError:
                    raise BadAttributeValueException(filename, "<rank>", '(val)', "(positive num)", "blank")
                rank = int(ch.text)
                if rank < 0:
                    raise BadAttributeValueException(filename, "<rank>", '(val)', "(positive num)", "negative")
            else:
                raise UndefinedElementException(filename, ch.tag)
        if 'rank' == -1:
            raise MissingElementException(filename, "<meta>", "rank")
        if (
            ('title' not in data) or
            ('desc' not in data) or 
            ('thumb' not in data)):
            raise MissingElementException(filename, "<meta>", "<title, desc, thumb>")
        if (
            (data['title'] is None) or
            (data['desc'] is None) or 
            (data['thumb'] is None)):
            raise BadAttributeValueException(filename, "(oneof) <title thumb desc rank>", '(val)', "non blank alphanumeruc", "blank")
        generated.append([rank, render_template(ITEM_FILE, **data)])
    return generated
