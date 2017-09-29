import numpy as np 
import geyserData as GD
import matplotlib.pyplot as pl 
import random

data = (GD.getData(0));


#pl.plot(data[:,0], data[:,1], 'o');
#pl.show(); 

#chose initial point in each cluster

p = np.zeros(2, dtype=np.int16 );
p[0] = random.randint(0, data.shape[0]);
p[1] = p[0];
while (p[1] == p[0]):
    p[1] = random.randint(0, data.shape[0]);
P = np.zeros((2,2));
P[0,:] = data[p[0],:];
P[1,:] = data[p[1],:];
print(P)


