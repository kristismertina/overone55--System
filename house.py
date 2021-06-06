class House:

    def __init__(self, area, price):
        self._area = area
        self._prise = price

    def final_price(self, sale):
        cost_sale = sale / 100
        return self._prise - self._prise * cost_sale


if __name__ == '__main__':
    h = House(121, 1000)
    print(h.final_price(20))