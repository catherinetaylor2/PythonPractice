from PIL import Image
import numpy as np

img = Image.open('cat.jpg');

#kernel = 1/16*np.array([[1,2,1], [2,4,2], [1,2,1]]);
kernel = np.array([[ 1, 0, -1], [0, 0, 0], [-1, 0, 1]]);
k = kernel.shape[1];
N = (k-1)//2;
I = Image.new(img.mode, img.size);

A = np.array(img);
E = np.pad(A, (N,N), 'reflect');

print(E.shape)
for y in range(0,img.size[0]):
    for x in range(0, img.size[1]):
        sum = np.array([0,0,0]);
        for i in range(0,k):
            for j in range(0,k):
                      sum = sum + E[x+2*N-i, y+2*N-j][1:4]*kernel[i,j];
        I.putpixel((y,x), (np.int(sum[0]),np.int(sum[1]),np.int(sum[2])));


I.show();





