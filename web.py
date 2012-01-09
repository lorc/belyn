#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import os.path
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from wsgiref.simple_server import make_server
from waitress import serve
from pyramid.session import UnencryptedCookieSessionFactoryConfig
import time
import player

@view_config(route_name='dashboard', renderer='dashboard.mako')
def dashboard_view(request):
    return {'time':time.asctime()}

@view_config(route_name='downloader', renderer='downloader.mako')
def downloader_view(request):
    return {'time':time.asctime()}

@view_config(route_name='player',renderer='player.mako')
def player_view(request):
    if request.method == "POST":
        if request.POST.get("file"):
            fname = request.POST["file"]
            if not os.path.exists(fname):
                request.session.flash(u"Файл '%s' не найден :("%fname)
            else:
                player.play(fname)
                return {"file":os.path.basename(fname),
                        "pos":player.get_pos()}
                pass
        else:
            request.session.flash(u"А что играть то?")
    return {}

@view_config(route_name="player_cmd")
def player_cmd(request):
    cmd = request.matchdict["cmd"]
    if cmd=="pause":
        player.pause()
    elif cmd=="stop":
        player.stop()
    elif cmd=="seek_left":
        player.seek(-5)
    elif cmd=="seek_right":
        player.seek(5)
    else:
        request.session.flash(u"Не знаю что за команда")
    return HTTPFound(location=request.route_url('player'))

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['mako.directories'] = os.path.join(here, 'templates')
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('idontgivemypassanybody')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_static_view('static', os.path.join(here, 'static'))
    config.add_route('dashboard','/')
    config.add_route('downloader','/downloader')
    config.add_route('player','/player')
    config.add_route('player_cmd','/player/{cmd}')
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    #server = make_server('0.0.0.0', 8080, app)
    #server.serve_forever()
    serve(app)
