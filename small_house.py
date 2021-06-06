from house import House
class SmallHouse (House):

    def __str__(self):
       return '({}, {}, {}, {})'.format(self._area)

    def __init__(self, prise):
        super().__init__(prise, 40)






