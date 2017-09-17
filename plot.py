import numpy as np 
import pylab as pl

x = np.zeros((200,));
y = np.zeros((200,));

j = 0;
for i in range(-100,100):
    x[j] = i;
    y[j] = i**2;
    j=j+1;

print(x);
print(y);

pl.plot(x,y);
pl.show(); 
