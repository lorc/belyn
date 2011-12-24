#!/usr/bin/python2
import pyexiv2
import os
import os.path
import wx
import random

class SlideshowFrame(wx.Frame):
    def __init__(self, parent, id, path):
        wx.Frame.__init__(self, parent, id, "", (0,0), wx.GetDisplaySize())
        self.SetBackgroundColour(wx.BLACK)
        self.Centre()
        self.path = path
        self.images = get_img_list(path)

        wx.EVT_PAINT(self, self.OnPaint)
        self.bitmap = None
        self.LoadImg(random.choice(self.images))

        self.timer = wx.Timer(self, -1)
        self.timer.Start(5000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

    def LoadImg(self, img_name):
        img = wx.Image(img_name)
        mt = pyexiv2.ImageMetadata(img_name)
        mt.read()
        orientation = 1
        if "Exif.Image.Orientation" in mt:
            orientation = mt["Exif.Image.Orientation"].value
        if orientation == 3:
            img = img.Rotate90().Rotate90()
        elif orientation == 6:
            img = img.Rotate90(True)
        elif orientation == 8:
            img = img.Rotate90(False)

        scrx, scry = wx.GetDisplaySize()
        imgx = img.GetWidth()
        imgy = img.GetHeight()
        imgratio = float(imgx) / imgy
        scrratio = float(scrx) / scry

        if imgratio > scrratio:
            scale = float(scrx) / imgx
        else:
            scale = float(scry) / imgy
        print "Scale", scale
#        if scale < 1:
        img.Rescale(int(imgx*scale), int(imgy*scale),wx.IMAGE_QUALITY_HIGH)
        print img.Width, img.Height
        self.bitmap = wx.BitmapFromImage(img)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.DrawImg(dc)

    def DrawImg(self, dc):
        if self.bitmap != None:
            scrx, scry = wx.GetDisplaySize()
            x = (scrx - self.bitmap.Width)  / 2
            y = (scry - self.bitmap.Height) / 2
            dc.DrawBitmap(self.bitmap,x,y)

    def OnTimer(self, event):
        self.LoadImg(random.choice(self.images))
        self.Refresh()

class MyApp(wx.App):
    def OnInit(self):
        frame = SlideshowFrame(None, -1, "/mnt/raid/photo")
        frame.Show(True)
        return True

def main():
    app = MyApp()
    app.MainLoop()


def get_img_list(path):
    ret = []
    for path, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".jpg") or f.endswith(".jpeg"):
                ret.append(os.path.join(path, f))
    return ret

def main__():
    mt = pyexiv2.ImageMetadata("/mnt/raid/photo/2010_03_09/20100309_IMG_6365.JPG")
    mt.read()
    if "Exif.Image.Orientation" in mt:
        print mt["Exif.Image.Orientation"].value
    files = get_img_list("/mnt/raid/photo")
    print "\n".join(files)

if __name__ == "__main__":
    main()
