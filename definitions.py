import flask
import json
import parameters


class QCM:
    def importfromclick(jsonform):
        pass


class deploy:
    def __init__(self) -> None:
        with open("./datafile.json", "r") as datafile:
            data = json.load(datafile)
            return (self, data)

    def unpack(self, **data):  # attention please, here is not correct
        for key in data:
            pass
