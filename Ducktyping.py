class Animal():
    def show(self):
        print("I am showing from animal")


class Human():
    def show(self):
            print("I am showing from  human")


obj = Animal()
obj2 = Human()

obj.show()
obj2.show()