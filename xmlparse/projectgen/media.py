from xmlparse.util import parse_link, ANIMATION, get_proj_assetfile
from xmlparse.exceptions import (MissingAttributeException, 
BadAttributeValueException, 
warn,
BadElementIndexException,
UndefinedElementException)

def create(elem, filename):
    if elem.tag == 'img' and 'cfg' not in elem.attrib:
        raise MissingAttributeException(filename, 'img', 'cfg')
    config_mode = elem.attrib['cfg'] if elem.tag == 'img' else None
    valid_modes = ['s', 'p']
    if elem.tag == 'img' and config_mode not in valid_modes:
        raise BadAttributeValueException(filename, 'img', 'cfg', valid_modes.join(', '), config_mode)

    imgfiles_raw = elem.attrib['i'].split('|') if elem.tag == "img" else elem.attrib['v']
    media_data = {
        'isImg': elem.tag == "img",
        'projfile' : get_proj_assetfile(filename),
        'media': imgfiles_raw,
        'config' : config_mode,
        'header' : [None, None],
        'caption': [None, None],
        'captionheaderexist' : False,
        'anim': ANIMATION
    }
    for ch in elem:
        if ch.tag == "h" or ch.tag == 'cap':
            key = 'header' if ch.tag == "h" else 'caption'
            if config_mode == 'p':
                if 'n' not in ch.attrib:
                    raise MissingAttributeException(filename, 'img', 'n')
                try:
                    n = int(ch.attrib['n']) if media_data['isImg'] else 1
                except ValueError:
                    raise ValueError("Bad n value for a header or content element while parsing " + filename + ".")
                if n != 1 and n != 2:
                    raise BadElementIndexException(filename, '<img> ==> (<header> or <caption>)', n)
                if ch.tag == "h" and media_data['header'][n-1] is not None:
                    raise BadElementIndexException(filename, '<header>', n)
                if ch.tag == 'cap' and media_data['caption'][n-1] is not None:
                    raise BadElementIndexException(filename, '<caption>', n)
                media_data[key][n-1] = parse_link(str(ch.text))
            else: #s
                media_data[key][0] = parse_link(str(ch.text))
        else:
            raise UndefinedElementException(filename, ch.tag)
    headercount = len([x for x in media_data['header'] if x is None])
    captioncount = len([x for x in media_data['caption'] if x is None])
    if headercount != captioncount:
        warn("Number of headers is not equal to the number of captions in a captioned <img> element in file " + filename + ".")
    media_data['captionheaderexist'] = not (
        all(v is None for v in media_data["caption"]) and all(v is None for v in media_data["header"])
        )
    return media_data