def myfunction():
    print("this is the first function")
myfunction()

def facebook(username, password):
    print("the username and password of facebook is %s and %s"%(username, password))
facebook("ganesh","neha")

# program for sum of two numbers #


def sum_of_numbers(a,b):
    return a+b
x = sum_of_numbers(3,4)
print(x)

#program on functions

def list_names():
    return "ganesh","neha","nirmala"

def love(name):
    print("%s loves dogs"%name)

def sentence():
    list_of_names = list_names()
    for name in list_of_names:
        print(love(name))
sentence()
