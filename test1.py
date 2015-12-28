import numpy as np

a=[]
n=5

for i in range(n*n):
    a.append(0)

a=np.array(a,int)

a=a.reshape((n,n))

ct=1
for i in a:
    try:
        i[ct]=1
        ct+=1
    except:
        a[n-1,0]=1
        a[n-1,1]=1
        a[n-1,2]=1
        break

print a

exp=2
x=np.dot(a,a)
if 0 in x:
    while 1>0:
        x=np.dot(x,a)
        exp+=1
        if 0 in x:
            print "exp is not" + str(exp)
            continue
        else:
            print "exp is " + str(exp)
            break

else:
    print "exp is " + str(2)


print x
