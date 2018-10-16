
class JsonParser:

    class Dummy:
        pass

    def __init__(self, data):
        self.result = self.parse(data)

    def parse(self, item):

        if type(item) is list:
            out=[]
            for info in item:
                out.append(self.parse(info))
        elif type(item) is dict:
            out = self.Dummy()
            for info in item.keys():
                out.__setattr__(info, self.parse(item[info]))
        else:
            out = item

        return out

class SpotifyObject:

    def __init__(self, data):
        parsed = JsonParser(data).result
        for attr in vars(parsed): self.__setattr__(attr, parsed.__getattribute__(attr))

    def print(self, fmt="%-20s : %-10s"):
        for attr in vars(self): print(fmt % (attr, self.__getattribute__(attr)))

class Device(SpotifyObject):
    id = ''
    is_active = False
    is_private_session = False
    is_restricted = False
    name = ''
    volume_percent = 0

class User(SpotifyObject):
    display_name = ''
    id = ''

class Track(SpotifyObject):
        
    def print(self, fmt="%-10s : %s"):

        print("")
        print(fmt % ('Track', self.name))
        print(fmt % ('Artist', self.artists[0].name))
        print(fmt % ('Album', self.album.name))


class Playlist(SpotifyObject):

    client = None
    fetched = False

    def __init__(self, data, client):
        self.client = client
        if 'owner' in data:
            self.user = User(data['owner'])
            del data['owner']
        super().__init__(data)

    def fetchTracks(self):
        self.tracks = self.client.user_playlist_tracks(self.user, self.id)
        self.fetched = True

    def print(self):
        pass

    


