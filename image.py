from PIL import Image


img = Image.open('cat.jpg');
#img.show();

r, g, b = img.split()
im = Image.merge("RGB", (b, g, r))

rgbIm = img.convert('RGB');
R,G,B = rgbIm.getpixel((0,0));

print(R,G,B);
