#!/usr/bin/python2
import os.path
import urllib
import urllib2
import urlparse
class Download(object):
    def __init__(self, link):
        self.url = link
        self.fname = ""
        self.full_size = None
        self.downloaded = 0
        self.f = None
        self.real_url = None
        self.out_f = None

    def start(self):
        self.f = urllib2.urlopen(self.url)
        self.real_url = self.f.geturl()
        self.full_size = int(self.f.info()["Content-Length"])
        print self.full_size
        fname = urllib.unquote(urlparse.urlparse(self.real_url).path)
        self.fname = os.path.split(fname)[1]
        print self.fname
        self.out_f = open(self.fname,"wb")
        while True:
            data = self.f.read(4096*4)
            if not data:
                break
            self.downloaded += len(data)
            self.out_f.write(data)
            print self.downloaded, "/", self.full_size, self.downloaded*100/self.full_size
        pass

if __name__ == "__main__":
    d = Download("http://www.ex.ua/get/9893564")
    d.start()
