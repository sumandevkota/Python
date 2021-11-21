#
# Example file for working with classes
#


class myclass():
    def method1(self):
        print("myClass method1")

    def method2(self,somestring):
        print("myClass method2 " + somestring)


class anotherclass(myclass):
    def method1(self):
        myclass.method1(self)
        print("anotherClass method1")

    def method2(self,somestring):
        print("anotherClass method2 ")

def main():
    c = myclass()
    c.method1()
    c.method2("this is a string")

    c2 = anotherclass()
    c2.method1()
    c2.method2("passed argument")

if __name__ == "__main__":
    main()
