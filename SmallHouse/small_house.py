from Human import House      #ModuleNotFoundError: No module named 'Human'

class SmallHouse:

    def __init__(self, small_area = 40.2):
        House.__init__(self, small_area)
        self.small_area = small_area



l = SmallHouse()
print(l.small_area)

#ModuleNotFoundError: No module named 'Human'