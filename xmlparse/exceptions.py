def warn(warning):
    print(warning) #prob make this red

class MetaNotFoundException(Exception):
    """
    Raised when project metadata is not found for a project.
    """
    
    def __init__(self, filename):
        super().__init__("missing metadata in XML file " + filename)

class MissingElementException(Exception):
    """
    Raised when a required sub-element is not found for an element.
    """
    
    def __init__(self, filename, elem, missing):
        super().__init__("Error while parsing " + filename + ". The element " + elem + " is missing the required <" + missing + "> element.")


class DuplicateElementException(Exception):
    """
    Raised when duplicate elem. when there isnt supposed to be.
    """

    def __init__(self, filename, elm, duped):
        super().__init__("Error while parsing" +  filename + ". The element " + duped + " must be a unique sub element of "+ elm + ".")

class BadElementIndexException(Exception):
    """
    Raised when an attribute is given a bad index or duplicate index to an existing one.
    """
    
    def __init__(self, filename, elm, index):
        super().__init__("Error while processing " + filename + ". Indexation attribute for element " + elm + " with index " + str(index) + " is either out of bounds, or a duplicate.")

class ShortDateFormatException(Exception):
    """
    Raised when bad date format
    """
    
    def __init__(self, filename, date):
        super().__init__("Error in file " + filename + ". Bad date: '" + date + "' is not formatted correctly.")

class ElementCountException(Exception):
    """
    Raised when an element has the wrong number of sub-elements. I.e., trying to fit 2 captions onto one image.
    """
    
    def __init__(self, fname, parent, expected, child, recv):
        super().__init__("Error while processing " + fname + ". Parent element " + parent + "expected " + expected + " elements of type " + child + " but recieved " + recv + ".")

class ElementOverflowException(Exception):
    """
    Raised when the number of sub-elements exceeds the max. number expected by parent element.
    """

    def __init__(self, fname, parent, max, child, recv):
        super().__init__("Error while processing " + fname + ". Parent element " + parent + "can only handle a maximum number of " + max + " elements of type " + child + " but recieved " + recv + ".")

class MissingAttributeException(Exception):
    """
    Raised when required attributes missing (i.e., an image is missing filename)
    """
    
    def __init__(self, filename, elem, attr):
        super().__init__("Error while processing file " + filename + ". The element " + elem + " expects an " + attr + " attribute but recieved none.")

class BadAttributeValueException(Exception):
    """
    Raised when an attribute is given a bad value (i.e., a number is too high for paragraphs, or an image is given 'R' as an arrangement)
    """

    def __init__(self, filename, elem, attrib, expected, recv):
        super().__init__("Error while processing file " + filename + ". The element " + elem + " expected one of " + expected + " as the value for " + attrib+ " but recieved " + recv + ".")

class UndefinedElementException(Exception):
    """
    Raised when an unidentified element is found
    """

    def __init__(self, filename, uelem):
        super().__init__("Error while processing file " + filename  +". Unidentified element '" + uelem + "'.")