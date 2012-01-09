#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os.path
import urllib
import urllib2
import urlparse
from threading import Thread

all_downloads = []

class Download(Thread):
    def __init__(self, link, save_d="."):
        Thread.__init__(self)
        self.url = link
        self.fname = ""
        self.full_size = None
        self.downloaded = 0
        self.f = None
        self.real_url = None
        self.out_f = None
        self.save_d = save_d
        global all_downloads
        all_downloads.append(self)
        self.state="created"

    def run(self):
        self.state="runing"
        self.f = urllib2.urlopen(self.url)
        self.real_url = self.f.geturl()
        self.full_size = int(self.f.info()["Content-Length"])
        print self.full_size
        fname = urllib.unquote(urlparse.urlparse(self.real_url).path)
        self.fname = os.path.split(fname)[1]
        print self.fname
        self.out_f = open(os.path.join(self.save_d, self.fname),"wb")
        while True:
            data = self.f.read(4096*4)
            if not data:
                break
            self.downloaded += len(data)
            self.out_f.write(data)
            print self.downloaded, "/", self.full_size, self.downloaded*100/self.full_size
        self.state="done"

if __name__ == "__main__":
    d = Download("http://www.ex.ua/get/9893564")
    d.start()
