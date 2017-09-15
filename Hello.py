import numpy as np 

print("hello world");

x = 3;

if x == 4:
    print("x is", 4);
else:
    print("x is not", 4);

f = 7.0;
g = float(7);

if f==g:
    print("match");

string = "HELLO";
print(string);

for i in range(0,5):
    print("x = ", i);

a = np.array([1,2,3]);
print("a = ", a);

for i in a:
    print(i**3);


def square(x):
    return x**2;

for i in (map(square, a)):
    print ("i = ", i);


