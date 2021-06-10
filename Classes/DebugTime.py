from datetime import datetime

now = datetime.now()

class DebugTime():
    """Class to redefine print"""
    def PrintMessage(message):
        print("{0}: {1}".format(now.time(), message))