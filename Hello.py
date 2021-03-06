import numpy as np 

print("hello world");

#IF LOOP
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

#FOR LOOPS
for i in range(0,5):
   print("x = ", i);

a = np.array([1,2,3]); #numpy array
print("a = ", a);
print("a type :", a.dtype);

for i in a:
    print(i**3);


def square(x):
    return x**2;

#MAP FUNCTION
for i in (map(square, a)):
   print ("i = ", i);


b = [square(x) for x in a];
print("b = ", b);

c = [*map(square,a)];
print("c = ", c);

#CONVERT TO ARRAY
B = np.array(b);
print("B =", B);
print(B.shape);