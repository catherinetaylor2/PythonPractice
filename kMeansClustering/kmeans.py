import numpy as np 
import geyserData as GD
import matplotlib.pyplot as pl 
import random

data = (GD.getData(0));


#pl.plot(data[:,0], data[:,1], 'o');
#pl.show(); 

#chose initial point in each cluster

p1 = random.randint(0, data.shape[0]);
p2 =p1;
while (p2 == p1):
 p2 = random.randint(0, data.shape[0]);
initialPoint1 = data[p1,:];
initialPoint2 = data[p2,:];

print(p1, p2)


