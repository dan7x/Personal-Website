from xmlparse.util import parse_link, ANIMATION
from xmlparse.exceptions import warn, BadAttributeValueException,UndefinedElementException,MissingAttributeException,BadElementIndexException

def create(elem, filename):
    
    arrangement = elem.attrib['arr']
    block_data = {
        'arrangement' : arrangement, #one of p, q (pair, quad)
        'headers' : [None, None, None, None],
        'body' : [None, None, None, None],
        'ANIM': ANIMATION
    }
    if arrangement not in ['p', 'q']:
        raise BadAttributeValueException(filename, 'block', 'arr', '{p, q}', arrangement)
    for ch in elem:
        
        if ch.tag == "h" or ch.tag == "cap":
            if 'n' not in ch.attrib:
                raise MissingAttributeException(filename, 'img', 'n')
            try:
                n = int(ch.attrib['n']) - 1
            except ValueError:
                raise ValueError("Bad n value for a header or content element while parsing " + filename + ".")
            if ((n < 0 or n > 3) and arrangement == 'q') or ((n < 0 or n > 1) and arrangement == 'p'):
                raise BadElementIndexException(filename, '<header> or <cap>', n + 1) 
            if block_data['headers'][n] is not None and ch.tag == "h": 
                raise BadElementIndexException(filename, '<header>', n + 1) 
            if block_data['body'][n] is not None and ch.tag == "cap":
                raise BadElementIndexException(filename, '<cap>', n + 1)
            tx = 'headers' if ch.tag == 'h' else 'body'
            block_data[tx][n] = parse_link(str(ch.text))
        else:
            raise UndefinedElementException(filename, ch.tag)
    block_data['block_content']=[[block_data["headers"][i], block_data["body"][i]] for i in range(0,4)]
    if len([x for x in block_data['headers'] if x is not None]) != len([x for x in block_data['body'] if x is not None]):
        warn("Unequal number of headers and body paragraphs in a <block> element.")
    return block_data