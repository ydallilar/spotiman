
import time
import threading
from spotiman.objects import Device, Track, JsonParser

"""
Simple implementation of a player class for spotiman
"""

class Player:

    devices = []
    current_device = 0
    status_thread = None
    track = None
    refresh_interval = 10 

    def __init__(self, client, refresh_interval=1):
        self.client = client
        self.refresh_interval = refresh_interval
        self.refresh()
        self.status_thread = threading.Thread(target=self.refreshRepeat)
        self.status_thread.start()

    def refresh(self):
        self.devices = [Device(device) for device in self.client.devices()['devices']]
        raw = self.client.currently_playing()
        if raw is not None:
            self.track = Track(self.client, raw=raw['item'])
            self.is_playing = raw['is_playing']
            self.progress_ms = raw['progress_ms']
        else:
            self.track = None

    def refreshRepeat(self):
        while True:
            time.sleep(self.refresh_interval)
            self.refresh()

    def play(self):
        self.client.start_playback()

    def pause(self):
        self.client.pause_playback()

    def next(self):
        self.client.next_track()

    def prev(self):
        self.client.previous_track()

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
            device.printDevice(fmt="    %-20s : %-10s")
 

