import numpy as np

''' 2 consecutive ones followed by a  01 ex: 11010,110100,............... it is actually 11010* with * replaced by a +'''
n =5
while n != 101:
    a = []
    for i in range(n * n):
        a.append(0)

    a = np.array(a, int)

    a = a.reshape((n, n))

    ct = 1
    for i in a:
        try:
            i[ct] = 1
            ct += 1
        except:
            a[n - 1, 0] = 1
            a[n - 1, 1] = 1
            a[n - 1, 2] = 0
            a[n - 1, 3] = 1
            a[n - 1, 4] = 0


            break
    exp = 2
    x = np.dot(a, a)
    while 0 in x:
        x = np.dot(x, a)
        exp += 1

    print "for n = " + str(n) + " the exponent is " + str(exp)
    n += 1
