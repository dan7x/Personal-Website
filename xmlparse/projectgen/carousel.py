from xmlparse.util import parse_link, ANIMATION,get_proj_assetfile
from xmlparse.exceptions import DuplicateElementException,UndefinedElementException,MissingElementException

def create(elem, filename):
    carousel_data = {
            'projfile' : get_proj_assetfile(filename),
            'slides':[],
            'ANIM': ANIMATION
        }
    for slide in elem: ## scroll delay?!
        if slide.tag == 'slide':
            if 'i' not in slide.attrib:
                raise MissingElementException(filename, '<slide>', 'i')
            cur_slide={
                'image' : slide.attrib['i']
            }
            for slide_elm in slide:
                if slide_elm.tag in cur_slide:
                    raise DuplicateElementException(filename, 'slide', slide_elm.tag)
                if slide_elm.tag == "h" or slide_elm.tag == "cap":
                    key = 'header' if slide_elm.tag == 'h' else 'caption'
                    cur_slide[key] = str(slide_elm.text)
                else:
                    raise UndefinedElementException(filename, slide_elm.tag)
            carousel_data["slides"].append(cur_slide)
        else:
            raise UndefinedElementException(filename, slide.tag)
    return carousel_data