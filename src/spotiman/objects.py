
from spotiman.utils import JsonParser

class Device:

    def __init__(self, data):
        for key in data.keys(): self.__setattr__(key, data[key])

    def printDevice(self, fmt="%-20s : %-10s"):
        for attr in vars(self): print(fmt % (attr, self.__getattribute__(attr)))


class Track:

    def __init__(self, sp, raw=None, id=None):

        if id is not None:
            raw = sp.track(id)
        elif raw is None:
            pass

        parsed = JsonParser(raw).result
        for attr in vars(parsed): self.__setattr__(attr, parsed.__getattribute__(attr))
        
    def printTrack(self, fmt="%-10s : %s"):

        print("")
        print(fmt % ('Track', self.name))
        print(fmt % ('Artist', self.artists[0].name))
        print(fmt % ('Album', self.album.name))


class Playlist:
 
    sp = None
    user = None
    id = None
    tracks = None
    fetched = False
    name = None

    def __init__(self, sp, user, id=id, name=name, fetch=False):

        self.sp = sp
        self.user = user
        self.id = id
        self.name = name
        if fetch:
            self.fetchInfo()

    def fetchInfo(self):
        self.fetchPlaylist()
        self.fetchTracks()

    def fetchPlaylist(self):
        raw = self.sp.user_playlist(self.user.id, playlist_id=self.id)
        parsed = JsonParser(raw).result
        for attr in vars(parsed): self.__setattr__(attr, parsed.__getattribute__(attr))
        
    def fetchTracks(self):
        raw = self.sp.user_playlist_tracks(self.user.id, self.id)
        self.tracks = [Track(self.sp, raw=raw_track['track']) for raw_track in raw['items']]
        self.fetched = True

class User:

    def __init__(self, raw):

        parsed = JsonParser(raw).result
        for attr in vars(parsed): self.__setattr__(attr, parsed.__getattribute__(attr))
        



