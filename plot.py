import numpy as np 
import matplotlib.pyplot as pl

x = np.zeros((20,));
y = np.zeros((20,));
z = np.zeros((20,));

j = 0;
for i in range(-10,10):
    x[j] = i;
    y[j] = i**2;
    z[j] = i**3;
    j=j+1;


plot1 = pl.plot(x,y, 'ro');
plot2 = pl.plot(x,z, 'bh');
pl.title('Look at this sweet graph');
pl.xlabel('x');
pl.ylabel('y');
pl.legend([plot1,plot2], ['1','2']);
pl.show(); 
