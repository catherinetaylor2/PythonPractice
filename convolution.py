from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('cat.jpg');
I = Image.new("RGB", img.size);


kernel = 1/16*np.array([[1,2,1], [2,4,2], [1,2,1]]); #gaussian blur
#kernel = np.array([[ 1, 0, -1], [0, 0, 0], [-1, 0, 1]]); #edge detection

k = kernel.shape[1];
N = (k-1)//2;

paddedImage = np.pad(np.array(img), (N,N), 'reflect');

for y in range(0,img.size[0]):
    for x in range(0, img.size[1]):
        sum = np.array([0,0,0]);
        for i in range(0,k):
            for j in range(0,k):
                      sum = sum + paddedImage[x+2*N-i, y+2*N-j][1:4]*kernel[i,j];
        I.putpixel((y,x), (np.int(sum[0]),np.int(sum[1]),np.int(sum[2]))); #PIL doesn't support floating point RGB


#Display before and after images
fig = plt.figure();
a = fig.add_subplot(1,2,1);
imgPlot = plt.imshow(img);
a.set_title('Original image');
a.set_yticklabels([]);
a.set_xticklabels([]);
a = fig.add_subplot(1,2,2);
imgPlot = plt.imshow(I);
a.set_title('Filtered image');
a.set_yticklabels([]);
a.set_xticklabels([]);

plt.show();





