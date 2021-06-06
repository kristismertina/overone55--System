from house import House
from buy_house import Human
from small_house import SmallHouse

class System:

    def __init__(self):
        self._humans = []
        self._houses = []


    def __str__(self):
       return '({}, {}, {}, {})'.format( self._humans, self._houses)

    def info (self):
        return 'Amount humans: {} \t Amount houses: {}'.format ((len(self._humans)),(len( self._houses)))

    def add_house (self,h):
        if isinstance(h, House):
            self._houses.append(h)
        else:
            raise TypeError


    def add_human (self, p):
        if isinstance(p, House):
            self._houses.append(p)
        else:
            raise TypeError


    def view_house(self):
        return self._houses

    def view_humans (self):
        return self._humans


    def creat_human ( self, name, age, money):
        if age < 150:
            if type(name) == str:
                return self.add_human(Human(money,name, age))
            else:
                raise TypeError ("Enter your name")
        else:
            raise ValueError ("Enter only number")


    def creat_house ( self, area, price):
        if type(area) == int and type(price) == int:
            return self.add_house(House(area, price))
        else:
            raise ValueError ("Enter only number")


    def creat_small_house (self, prise):
            return self.add_house(SmallHouse(prise))














if __name__ == '__main__':

    hu1 = System()
    # hu2 = System()
    # hu1.add_human("Vasya")
    # hu2.add_human("Petsya")
    # print(hu1.view_humans())
    # print(hu2.view_humans())
    #
    # ha1 = System()
    # ha2 = System()
    # hu1.add_house("40.2")
    # hu2.add_house(34343)
    # print(hu1.view_house())
    # print(hu2.view_house())

    # print (hu1.creat_human("hghg", 87, 8787))
    # print(hu1.creat_house("hghg", 87, 8787))
    print(hu1.creat_small_house(67))
    print(hu1._houses)
    print (System.info)

