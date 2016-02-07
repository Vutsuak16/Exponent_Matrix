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
a[3][5] = 1
a[4][3] = 1
a[5][3] = 1
a[5][6] = 1
a[6][5] = 1

y = a
ct = 100  # even on 1000 interations we dont get a positive matrix therefore we need to put self loops
while ct > 0:
    x = a
    y = np.dot(x, y)
    if 0 not in y:
        print "exponent reached self loop not required"
        break
    ct -= 1


'''a[0][0] = 1  # self loop put at vertex 1
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
a[1][1] = 1  # self loop put at vertex 2
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
'''a[2][2] = 1  # self loop put at vertex 3
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

a[3][3] = 1  # self loop put at vertex 4
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
a[4][4] = 1  # self loop put at vertex 5
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
a[5][5] = 1  # self loop put at vertex 6
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
'''a[6][6] = 1  # self loop put at vertex 7
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



