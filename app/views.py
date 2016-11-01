from flask import render_template
from app import mantag

@mantag.route('/')
@mantag.route('/index')
def index():
    obj = {
        'title': 'Mumford & Sons',
        'description': 'Mumford & Sons is a bluegrass/folk/indie band founded in Londom...',
        'img': 'http://img2-ak.lst.fm/i/u/avatar300s/e125f7a6fe204e18ce018d5f714877ad.jpg',
        'tags': ['folk', 'indie', 'british', 'bluegrass', 'free', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', ]
    }
    return render_template('index.html', obj=obj)
