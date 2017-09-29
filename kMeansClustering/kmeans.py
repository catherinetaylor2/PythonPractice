import numpy as np 
import geyserData as GD
import matplotlib.pyplot as pl 

data = GD.getData(0);

pl.plot(data[:,0], data[:,1], 'o');
pl.show(); 


