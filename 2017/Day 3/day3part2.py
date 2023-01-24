val = 289326

class Spiral:
    def __init__(self):
        self._data = {(0, 0): 1, (1, 0): 1}
    
    def build(self, checkVal):
        while max(self._data.values()) <= checkVal:
            pass