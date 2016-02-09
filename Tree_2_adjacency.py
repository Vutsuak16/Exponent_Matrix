import numpy as np

n = 18

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
a[3][5] = 1
a[3][6] = 1
a[4][3] = 1
a[5][3] = 1
a[6][3] = 1
a[6][7] = 1
a[6][8] = 1
a[6][9] = 1
a[7][6] = 1
a[8][6] = 1
a[9][6] = 1
a[9][10] = 1
a[9][11] = 1
a[9][12] = 1
a[10][9] = 1
a[11][9] = 1
a[12][9] = 1
a[12][13] = 1
a[12][14] = 1
a[13][12] = 1
a[14][12] = 1
a[15][12] = 1
a[15][16] = 1
a[15][17] = 1
a[16][15] = 1
a[17][15] = 1

y = a
ct = 100  # even on 1000 interations we dont get a positive matrix therefore we need to put self loops
while ct > 0:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent reached self loop not required"
        break
    ct -= 1

a[0][0] = 1  # self loop at all exponents
a[1][1] = 1
a[2][2] = 1
a[3][3] = 1
a[4][4] = 1
a[5][5] = 1
a[6][6] = 1
a[7][7] = 1
a[8][8] = 1
a[9][9] = 1
a[10][10] = 1
a[11][11] = 1
a[12][12] = 1
a[13][13] = 1
a[14][14] = 1
a[15][15] = 1
a[16][16] = 1
a[17][17] = 1

y = a
ct = 0
while ct != 5:
    x = a
    print y
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
