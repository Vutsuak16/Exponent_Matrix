import numpy as np

n = 13

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
a[10][9] = 1
a[11][9] = 1
a[11][12] = 1
a[12][11] = 1
y = a

ct = 100  # even on 1000 interations we dont get a positive matrix therefore we need to put self loops
while ct > 0:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent reached self loop not required"
        break
    ct -= 1

'''a[0][0] = 1  # self loop put at vertex 1 , exponent is 10
y = a
ct = 0
while ct != 1000:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''

'''
a[1][1] = 1  # self loop put at vertex 2 exponent is 8
y = a
ct = 0
while ct != 1000:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1

'''
'''
a[2][2] = 1  # self loop put at vertex 3 exponent is 10
y = a
ct = 0
while ct != 1000:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''
'''
a[3][3] = 1  # self loop put at vertex 4 exponent is 6
y = a
ct = 0
while ct != 1000:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1

'''
'''
a[4][4] = 1  # self loop put at vertex 5 exponent is 8
y = a
ct = 0
while ct != 1000:
    x = a
    y = np.dot(x, y)

    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''
'''
a[5][5] = 1  # self loop put at vertex 6 exponent is 8
y = a
ct = 0
while ct != 1000:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''
'''
a[6][6] = 1  # self loop put at vertex 7 exponent is 4
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''

'''
a[7][7] = 1  # self loop put at vertex 8 exponent is 6
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1

'''
'''
a[8][8] = 1  # self loop put at vertex 9 exponent is 6
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1

'''
'''
a[9][9] = 1  # self loop put at vertex 10 exponent 6
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''
'''
a[10][10] = 1  # self loop put at vertex 11 exponent 8
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1

'''
'''
a[11][11] = 1  # self loop put at vertex 12 exponent 8
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1

'''
'''
a[12][12] = 1  # self loop put at vertex 13 exponent 10
y = a
ct = 0
while ct != 100:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent is " + str(ct)
        print y
        break
    ct += 1
'''
