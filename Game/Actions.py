import copy
from dlgo.gotypes import Player

class Move():
    def __init__(self,point=None,is_pass=False,is_resign=False):
        assert(point is not None)^is_pass^is_resign
        self.point=point
        self.is_pass=is_pass
        self.is_resign=is_resign

    @classmethod
    def play(cls,point):
        return Move(point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)