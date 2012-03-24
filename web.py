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
import media
import smart

class lamp_state:
    def __init__(self, idx, state):
        self.idx=idx
        self.state=state
    pass

@view_config(route_name='dashboard', renderer='dashboard.mako')
def dashboard_view(request):
    lamps=[]
    lamps_state = smart.get_state()
    lamps.append(lamp_state(0, lamps_state & 1 == 1))
    lamps.append(lamp_state(1, lamps_state & 2 == 2))

    return {'time':time.asctime(),'lamps':lamps,'lamp_state':lamps_state}

@view_config(route_name='downloader', renderer='downloader.mako')
def downloader_view(request):
    return {'time':time.asctime()}

@view_config(route_name='player',renderer='player.mako')
def player_view(request):
    if request.method == "POST":
        if request.POST.get("file"):
            fname = request.POST["file"]
            if not os.path.exists(fname):
                pass
                #request.session.flash(u"Файл '%s' не найден :("%fname)
            else:
                player.play(fname)
                return {"file":os.path.basename(fname),
                        "pos":player.get_pos(),
                        "media":media.get()}
        else:
            request.session.flash(u"А что играть то?")
    return {"media": media.get()}

@view_config(route_name="player_cmd")
def player_cmd(request):
    if not player.playing():
        request.session.flash(u"А плеер то не играет!")
        return HTTPFound(location=request.route_url('player'))

    cmd = request.matchdict["cmd"]
    if cmd=="pause":
        player.pause()
    elif cmd=="stop":
        player.stop()
    elif cmd=="seek_left":
        player.seek(-5)
    elif cmd=="seek_right":
        player.seek(5)
    elif cmd=="snd_up":
        player.volume(5)
    elif cmd=="snd_down":
        player.volume(-5)
    else:
        request.session.flash(u"Не знаю что за команда")
    return HTTPFound(location=request.route_url('player'))

@view_config(route_name="lights_cmd")
def lights_cmd(request):
    cmd = request.matchdict["cmd"]
    idx = int(request.matchdict["idx"])
    intf = smart.get_interface()
    if not intf:
        request.session.flash(u"Аппаратный сбой!")
        return HTTPFound(location=request.route_url('dashboard'))
    state = smart.get_state()
    if cmd == 'toggle':
        if idx<0:
            if state:
                smart.turn_off(intf)
            else:
                smart.turn_on(intf)
        else:
            state = state ^ (1<<idx)
            smart.set_state(state, intf)
    return HTTPFound(location=request.route_url('dashboard'))

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
    config.add_route('lights_cmd','/light/{idx}/{cmd}')
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    #scan for media
    media.scan()
    #start server
    serve(app)
