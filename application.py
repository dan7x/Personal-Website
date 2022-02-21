from flask import Flask, render_template,abort
from xmlparse.parser import generate
from xmlparse.listgen import generate_project_list
from xmlparse.util import gFirst

application = Flask(__name__)

def skeletal_render(page, **kwargs):
    return render_template('skeletons/pages/' + str(page), **kwargs)

@application.route("/")
def home():
    data = {
    'title' : 'Home',
    'metacontent' : 'Daniel Xiao: Home',
    'css_filename' : 'Home'
    }
    return skeletal_render("index.html", **data)

@application.route("/projects")
@application.route("/projects/<proj>")
def projects(proj=None):
    try:
        if proj == None:
                pgen = generate_project_list('projects')
                pgen.sort(key=gFirst, reverse=True)
                data_home = {
                'title' : 'Projects',
                'metacontent' : 'ProjectHub',
                'css_filename' : 'ProjectHub',
                'main_content' : [item[1] for item in pgen],
                'is_iproj' :True
                }
                return skeletal_render("ProjectHub.html", **data_home)
        data = {
            'title' : proj,
            'metacontent' : 'Projects'+ str(proj),
            'css_filename' : 'ProjectPreviewer',
            'main_content' : generate("projects/" + proj)
        }
        return skeletal_render("ProjectPreviewer.html", **data)
    except FileNotFoundError:
            abort(404)

@application.route("/notes")
@application.route("/notes/<note>")
def notes(note = None):
    abort(404) #for now
    if note == None:
        return "notes"
    return "notes of " + str(note)

@application.route("/construction")
def construction(proj=None):
    data = {
    'title' : 'Under Construction',
    'metacontent' : 'ComingSoon',
    'css_filename' : 'ComingSoon'
    }
    return skeletal_render("ComingSoon.html", **data)

@application.errorhandler(404)
def page_not_found(e):
    data={
        'css_filename' : 'ComingSoon',
        'error':{
            'title':'404 file not found',
            'desc':'we didnt find ur file.'
        }
    }
    return skeletal_render('error.html',**data), 404

# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    # application.debug = True
    application.run()
