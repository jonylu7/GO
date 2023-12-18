
 class GoString():
     def __init__(self,color,stones,liberties):
         self.color=color
         self.stones=set(stones)
         self.liberties=set(liberties)
     def remove_liberty(self,point):
         self.liberties.remove(point)

     def add_liberty(self,point):
         self.liberties.add(point)

     def merged_with(self,go_string):
         assert go_string.color==self.color
         combined_stones=self.stones | go_string.stones
         return GoString(self.color,combined_stones,(self.liberties | go_string.liberties)-combined_stones)

    @property
    def num_liberties(self):
     return len(self.liberties)

    def __eq__(self,other):
        return isinstance(other,GoString) and \


