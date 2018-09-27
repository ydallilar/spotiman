
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


