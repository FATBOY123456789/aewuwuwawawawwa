class COMPUTA:
    def __init__(self):
        self.__max_price=500
    def sell(self):
        print('The value of the computer is : ',self.__max_price)
    def setmaxprice(self,price):
        self.price=price
        self.__max_price=price
c=COMPUTA()
c.sell()
# changing the price :)
c.setmaxprice(1000)
c.sell()