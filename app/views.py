from flask import render_template
from app import mantag

@mantag.route('/')
@mantag.route('/index')
def index():
    obj = {
        'title': 'Mumford & Sons',
        'description': 'Mumford & Sons é uma banda de bluegrass/folk/indie fundada em Londres, Inglaterra em dezembro de 2007. Surgiu de um fenômeno que alguns da mídia local chamavam de “cena folk do oeste de Londres”, junto com artistas como Laura Marling, Johnny Flynn e Noah and the Whale. O grupo gravou um EP, Love Your Ground, e começou uma turnê no Reino Unido para ganhar audiência para sua música, ganhando suporte para um eventual álbum.'
    } 
    tags = ['folk', 'indie', 'british', 'bluegrass', 'free', 'test']
    return render_template('index.html', obj=obj, tags=tags)