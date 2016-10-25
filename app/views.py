from flask import rende_template
from app import mantag

@mantag.route('/')
@mantag.route('/index')
def index():
    obj = {
        'title': 'Mumford & Sons'
        'description': 'Mumford & Sons é uma banda de bluegrass/folk/indie fundada em Londres, Inglaterra em dezembro de 2007. Surgiu de um fenômeno que alguns da mídia local chamavam de “cena folk do oeste de Londres”, junto com artistas como Laura Marling, Johnny Flynn e Noah and the Whale.'
        'tags': 'indie', 'folk', 'acustic', 'bluegrass'
    } 
    return rende_template('index.html' obj=obj)