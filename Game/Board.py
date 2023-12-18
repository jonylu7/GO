class Board():
    def __init__(self,num_rows,num_cols):
        self.num_rows=num_rows
        self.num_cols=num_cols
        self._grid={}

    def place_stone(self,player,point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None


    def is_on_grid(self,point):