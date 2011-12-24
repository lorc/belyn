#!/usr/bin/python2
import wx
import time
class ClockFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "", wx.DefaultPosition, wx.GetDisplaySize())

        box = wx.BoxSizer(wx.HORIZONTAL)
        self.SetCursor(wx.StockCursor(wx.CURSOR_BLANK))
        self.SetBackgroundColour(wx.BLACK)
        self.clock_tx = wx.StaticText(self, -1, "00:00:00", style = wx.RIGHT)

        box.Add(self.clock_tx,0,wx.ALIGN_CENTER|wx.LEFT)
        self.SetSizer(box)
        self.clock_tx.SetForegroundColour(wx.GREEN)
        font = wx.Font(200, wx.DEFAULT, wx.NORMAL, 0)
        self.clock_tx.SetFont(font)
        self.clock_tx.Center()
        self.clock_tx.SetCursor(wx.StockCursor(wx.CURSOR_BLANK))

        self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.Centre()
    def OnTimer(self, event):
        t = time.localtime(time.time())
        st = time.strftime("%H:%M:%S",t)
        self.clock_tx.SetLabel(st)

class BelynApp(wx.App):
    def OnInit(self):
        frame = ClockFrame(None, -1)
        frame.Show(True)
        return True

def main():
    app = BelynApp()
    app.MainLoop()

if __name__ == "__main__":
    main()
