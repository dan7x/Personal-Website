from xmlparse.util import parse_link, ANIMATION

def create(elem, filename):
    parsed_text = parse_link(str(elem.text))
    text_data = {
        'content': parsed_text,
        'anim': ANIMATION
    }
    return text_data