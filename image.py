from PIL import Image
import numpy as np 


img = Image.open('cat.jpg');
#img.show();

r, g, b = img.split()
im = Image.merge("RGB", (b, g, r))

rgbIm = img.convert('RGB');
R,G,B = rgbIm.getpixel((0,0));

 #print(R,G,B);

I = Image.new(img.mode, (500,500));
#rI, gI, bI = I.split();


for i in range(0,500):
    for j in range(0,500):
        I.putpixel((i,j),(255,0,0));

#I = Image.merge("RGB", (rI, gI, bI));
I.show();