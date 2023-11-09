import enum


class Player(enum.Enum):
    black=1
    white=2

    @property
    def switch(self):
        if self==Player.white:
            return Player.black
        else:
            return Player.white
