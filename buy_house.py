class Human:
    default_name = "Vasya"
    default_age = "30"

    def __init__(self, house, money,  name = default_name, age = default_age):
        self.__name = name
        self.__age = age
        self.__house = []
        self.__money = money

    def __str__(self):
       return '({}, {}, {}, {})'.format(self.__name, self.__age, self.__house, self.__money )


    def info (self):
        print("Human")
        print("Name:" + self.__name)
        print("Age:" + self.__age)
        print("House:" + self.__house)    # здесь потомучто список?
        print("Money:" + self.__money)

    @staticmethod
    def default_info():
        print('({}, {}, {}, {})'.format(default_name, default_age))

    @property
    def __make_deal(self, house, cost):
        return self.__money - cost

    @property
    def __earn_money(self, total):
        return self.__money + total

    @property
    def __buy_house(self, house, sale):
        try:
            self.__make_deal(house, house.sale (sale))
        except:
            ValueError ("num")


    # не понимаю что здесь писать
        #if self.__money >=
        return self.__house.append(house)

class House:

    def __init__(self, area, price):
        self._area = area
        self._prise = price

    def final_price(self, sale):
        return self._prise - sale






obj = Human("1212", 7)
o = House (4, 60)

#print(o.final_price())
#print(obj.__earn_money(5))  #AttributeError: 'Human' object has no attribute '__earn_money'
#print(obj.default_info())  #NameError: name 'default_name' is not defined
print(obj.info()) #TypeError: can only concatenate str (not "list") to str
                  #здесь я понимаю нужно список в строку преобразовть


Word = str(self.__house[0])
print("I like the {0} ...".format(Word))