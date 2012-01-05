#!/usr/bin/python2

import os
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from wsgiref.simple_server import make_server
from pyramid.session import UnencryptedCookieSessionFactoryConfig
import time

@view_config(route_name='dashboard', renderer='dashboard.mako')
def dashboard_view(request):
    return {'time':time.asctime()}

@view_config(route_name='downloader', renderer='downloader.mako')
def downloader_view(request):
    return {'time':time.asctime()}

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
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
