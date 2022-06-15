class Mylove:    # class template
    name = "ganesh"   #variables inside the class

    def function(self):  #function inside the class
        print("ganesh loves neha")

object = Mylove() #object is an encapsulation of variable and functions into single entity
print(object.name)
object.name = "nirmala"
print(object.name)
print(object.function())
