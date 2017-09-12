class C(object):
    vv = 10
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
c1 = C(10)
# print(c1.__value)
c1.show()
