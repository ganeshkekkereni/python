x=1
if x==1:
    print("value of x is 1")
    
one = 1
two = 2
three = one+two
print(three)

name = "ganesh"
name2 = "neha"
name3 = name + " " + name2
print(name3)

a = "ganesh"
print("hello, %s!"%a)

n = "ganesh"
age = 20
print("hello %s your age is %d"%(n, age))

name1 = "ganesh"
age1 = 20
if name1 == "ganesh" and age1 == 20:
    print("ganesh having age of 20")
if name1 == "ganesh" or name1 == "neha":
    print("ganesh loves neha")
    
s = ["ganesh", "neha"]
n1 = "ganesh"
if n1 in s:
    print("ganesh is present in s list")
    
primes = [2,3,5,7]
for prime in primes:
    print(prime)
    
for i in range(5):
    print(i)

for i in range(3,9):
    print(i)
for i in range(3,9,2):
    print(i)
    
count = 0
while count<5:
    print(count)
    count += 1


b = 0
while True:
    print(b)
    b += 1
    if b<=5:
        break
for c in range(10):
    if c%2==0:
        continue
    print(c)


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

z=0
while(z<5):
    print(z)
    z +=1
else:
    print("count value reached %d" %(z))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
