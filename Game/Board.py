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

        for same_color_string in adjacent_same_color:
            new_string=new_string.merged_with(same_color_string)

        for new_string_point in new_string.stones:
            self._grid[new_string_point]=new_string

        for opposite_color_string in adjacent_opposite_color:
            opposite_color_string.remove_liberty(point)

        for opposite_color_string in adjacent_opposite_color:
            if(opposite_color_string.num_liberties==0):
                self._remove_string(opposite_color_string)

    def _remove_string(self,string):
        for point in string.stones:
            for neighbor in point.neighbors():
                neighbor_strings=self._grid.get(neighbor)
                if(neighbor_strings is None):
                    return None
                else:
                    neighbor_strings.add_liberty(point)


    def is_on_grid(self,point):
        return (1<=point.row<=self.num_rows) and (1<=point.col<=self.num_cols)

    def get_go_string(self,point)->GoString:
        string=self._grid.get(point)
        if(string is None):
            return None
        else:
            return string

    def get(self,point)->GoString.color:
        string=self._grid.get(point)
        if(string is None):
            return None
        else:
            return string.color



