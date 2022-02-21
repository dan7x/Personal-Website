## Generates new project using cmd line
from shutil import copyfile
import sys
import os

disallowed = ['/', '\\', ':', '*', "?", '"', "<", ">", "|"]

arg = " ".join(sys.argv[1:])
if any([x for x in disallowed if x in arg]):
    raise ValueError("Filename with disallowed characters: all of " + str(disallowed) + " are disallowed.")

dirname = os.path.dirname(__file__)
ass_folder_name = os.path.join(dirname, 'static/projassets/' + arg)
xml_orig = os.path.join(dirname, 'templates/base.xml')
xml_copy = os.path.join(dirname, 'projects/' + arg + ".xml")
os.mkdir(ass_folder_name)
print("Assetfolder directory created at " + ass_folder_name)
copyfile(xml_orig, xml_copy)
print("XML template created at " + xml_copy)