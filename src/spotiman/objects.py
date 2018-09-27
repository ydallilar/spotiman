
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
        if raw is None:
            pass

        parsed = JsonParser(raw).result
        for attr in vars(parsed): self.__setattr__(attr, parsed.__getattribute__(attr))
        
    def printTrack(self, fmt="%-10s : %s"):

        print("")
        print(fmt % ('Track', self.name))
        print(fmt % ('Artist', self.artists[0].name))
        print(fmt % ('Album', self.album.name))


