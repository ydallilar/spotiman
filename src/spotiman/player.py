
import time
import threading
from spotiman.objects import Device, Track, User, Playlist
import logging
import json

"""
Simple implementation of a player class for spotiman
"""

class Player:

    devices = []
    current_device = 0
    status_thread = None
    track = None
    refresh_interval = 10 
    progress_ms = 0
    volume_percent = 0
    is_playing = False
    kill = False

    def __init__(self, client, refresh_interval=1):
        self.client = client
        self.refresh_interval = refresh_interval
        self.fetchMe()
        self.refresh()

    def refresh(self):
        self.fetchDevices()
        self.fetchCurrentPlayback()

    def refreshRepeat(self):
        while True:
            if self.kill:
                break
            self.refresh()
            time.sleep(self.refresh_interval)           

    def start(self):
        self.status_thread = threading.Thread(target=self.refreshRepeat)
        self.status_thread.start()

    def shutdown(self):
        self.kill = True
        self.status_thread.join()

    def fetchDevices(self):
        self.devices = self.client.devices()
        for device in self.devices: logging.debug(device.id)

    def fetchMe(self):
        self.me = self.client.me()
        logging.debug('Fetching user %s' % self.me.id)

    def fetchCurrentPlayback(self):
        track, info = self.client.current_playback()
        if info is not None:
            self.track = track
            self.is_playing = info['is_playing']
            self.progress_ms = info['progress_ms']
            self.device = Device(info['device'])
        else:
            logging.warning("Failed to get current playback")
            self.track = None
            self.device = None

    def fetchPlaylists(self):
        self.playlists = self.client.current_user_playlists()
        logging.debug('Fetching user playlist information.')

    def selectDevice(self, index):
        logging.debug("Setting current device to {%s:%s}" % (self.devices[index].id, self.devices[index].name))
        self.client.transfer_playback(self.devices[index].id)

    def play(self):
        self.client.start_playback()

    def pause(self):
        self.client.pause_playback()

    def next(self):
        self.client.next_track()

    def prev(self):
        self.client.previous_track()

    def seekAbs(self, amount):
        self.client.seek_track(amount)

    def seekRel(self, amount):
        self.client.seek_track(self.progress_ms + int(amount*1e3))

    def stop(self):
        self.seekAbs(0)
        self.pause()

    def getVolume(self):
        if self.device is not None:
            return self.device.volume_percent
        else:
            return 0

    def setVolume(self, perc):
        self.client.volume(perc)

    def setRelVolume(self, perc):
        self.client.volume(self.device.volume_percent + perc)

    def getDurationMMSS(self):
        return "%2d:%02d" % ((self.progress_ms/1000.) / 60, (self.progress_ms/1000.) % 60)

    def getProgressMMSS(self):
        return "%2d:%02d" % ((self.track.duration_ms/1000.) / 60, (self.track.duration_ms/1000.) % 60)

    def printStatus(self, fmt="%2d:%02d/%2d:%02d %-2s %s - %s"):
        status = '|>' if self.is_playing else '||'
        prog_s = (self.progress_ms/1000.) % 60
        prog_m = (self.progress_ms/1000.) / 60
        dur_s = (self.track.duration_ms/1000.) % 60
        dur_m = (self.track.duration_ms/1000.) / 60
        print(fmt % (prog_m, prog_s, dur_m, dur_s, status, 
            self.track.artists[0].name, self.track.name))

    def printDevices(self):
        print("\nAvailable Devices:")
        for i, device in enumerate(self.devices):
            ndx_fmt = "%2d => "
            if device.is_active: ndx_fmt = "*" + ndx_fmt
            print(ndx_fmt % i)
            device.print(fmt="    %-20s : %-10s")
 

