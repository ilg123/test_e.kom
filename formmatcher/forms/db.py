from tinydb import TinyDB, Query


db = TinyDB('db.json')
FormTemplate = Query()

def get_form_templates():
    return db.all()

def add_form_template(name, fields):
    db.insert({'name': name, 'fields': fields})

def remove_all_templates():
    db.truncate()
