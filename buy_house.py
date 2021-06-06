from house import House

class Human:
    __default_name = "Vasya"
    __default_age = 30

    def __init__(self, money,  name = __default_name, age = __default_age):
        self.__name = name
        self.__age = age
        self.__house = []
        self.__money = money

    def __str__(self):
       return '({}, {}, {}, {})'.format(self.__name, self.__age, self.__money, self.__house)


    def info (self):
        return 'Name: {} \t Age: {} \t House:{} \t Money: {}'.format(self.__name, self.__age, self.__money, self.__house )


    @staticmethod
    def default_info():
        return 'Name: {} \t Age: {}'.format(Human.__default_name, Human.__default_age)


    def __make_deal(self, house, cost):
        if self.__money >= cost:
            self.__money -= cost
            self.__house.append(house)
            return True
        else:
            raise ValueError("Insufficient funds")


    def earn_money(self, total):
        return self.__money + total


    def buy_house(self, house, sale):
        try:

            return  self.__make_deal(house, house.final_price(sale))
        except Exception as e:
           return e




if __name__ == '__main__':

    obj = Human(10000)
    #print(obj.earn_money(1000))
    #print(obj.default_info())


    h1 = House (42, 113)
    #print(h1._prise)
    print (obj.buy_house (h1, 10))

    #print(obj.default_info())


