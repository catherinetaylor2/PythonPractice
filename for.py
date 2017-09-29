import numpy as np 

a = np.array(["one","two","three"]);

for i in a:
    print(i);

for j in range(len(a)):
    print("j =",j);
    print("a[j] = ", a[j])

for i in range(2,10):
    if (i % 2 == 0):
        print("even", i);
        continue; #skips back to start of loop
    print("odd", i)
