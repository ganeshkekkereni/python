class numberholder:

    def __init__(self, number):
        self.number = number
    def returnnumber(self):
        return self.number

object = numberholder(7)
print(object.returnnumber())

class string:

    def __init__(self, name):
        self.name=name
    def returnname(self):
        return self.name

x = string("ganesh")
print(x.returnname())
