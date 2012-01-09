#!/usr/bin/python2
import mpylayer
import time

player = None

if __name__=="__main__":
    mp = mpylayer.MPlayerControl()
    mp.loadfile("/mnt/raid/anime/Wolf and Spices/Season 1/10.mkv")
    mp.volume = 0
    mp.fullscreen = 1
    print mp.sub_demux
    print mp.metadata
    time.sleep(10)
    mp.sub_select()
    time.sleep(10)
    mp.sub_select()
    time.sleep(10)
    mp.sub_select()

def play(fname):
    global player
    stop()
    player = mpylayer.MPlayerControl()
    player.loadfile(fname)
    player.volume = 0
    player.fullscreen = 1

def pause():
    player.pause()
def seek(t):
    player.seek(t)
def stop():
    global player
    if player:
        player.quit()
    player=None

def get_pos():
    if player:
        return player.time_pos
    return None
