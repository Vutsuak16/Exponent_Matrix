import numpy as np

n = 7

a = [0 for i in range(n ** 2)]

a = np.array(a, int)
a = a.reshape((n, n))

a[0][1] = 1
a[1][0] = 1
a[1][2] = 1
a[1][3] = 1
a[2][1] = 1
a[3][1] = 1
a[3][4] = 1
a[4][3] = 1
a[4][5] = 1
a[4][6] = 1
a[5][4] = 1
a[6][4] = 1

y = a
ct = 100  # even on 1000 interations we dont get a positive matrix therefore we need to put self loops
while ct > 0:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent reached self loop not required"
        break
    ct -= 1

# a[0][0] = 1
# a[1][1] = 1
# a[2][2] = 1
a[3][3] = 1
# a[4][4] = 1
# a[5][5] = 1
# a[6][6] = 1

y = a
ct = 1
print y
while ct != 1000:
    x = a
    j = y
    y = np.dot(x, y)
    ct += 1
    if 0 not in y:
        print j
        print "exponent is " + str(ct)
        print y
        break
