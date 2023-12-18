from GroupTracking import GoString

class Board():
    def __init__(self,num_rows,num_cols):
        self.num_rows=num_rows
        self.num_cols=num_cols
        self._grid={}

    def place_stone(self,player,point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None
        adjacent_same_color=[]
        adjacent_opposite_color=[]
        liberties=[]
        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string=self._grid.get(neighbor)
            if(neighbor_string is None):
                liberties.append(neighbor)
            elif neighbor_string.color==player.color:
                if neighbor_string not in adjacent_same_color:
                    adjacent_same_color.append(neighbor)
            else:
                if neighbor_string not in adjacent_opposite_color:
                    adjacent_opposite_color.append(neighbor)
        new_string=GoString(player,[point],liberties)



    def is_on_grid(self,point):
        return (1<=point.row<=self.num_rows) and (1<=point.col<=self.num_cols)

    def get_go_string(self,point):
        string=self._grid.get(point)
        if(string is None):
            return None
        else:
            return string

    def get(self,point):
        string=self._grid.get(point)
        if(string is None):
            return None
        else:
            return string.color



