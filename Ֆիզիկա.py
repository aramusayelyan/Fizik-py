
while True:
    import math
    a=0
    v=0
    t=0
    s=0
    g=10
    j=input('Անհայտ')
    if j==('a'):
        v=eval(input('V'))
        l=input('Միավոր')
        t=eval(input('T'))
        p=input('Միավոր')
        if l==('կմ/ժ'):
            v=v*3.6
        if p==('ժ'):
            t=t*60
        if v==0:
            s=input('S')
            v=s/t
        if t==0:
            s=input('S')
            t= math.sqrt(2*s/g)
        print ('A=',v/t)
    if j==('s'):
        v=eval(input('V'))
        l=input('Միավոր')
        t=eval(input('T'))
        p=input('Միավոր')
        if l==('կմ/ժ'):
            v=v*3.6
        if p==('ժ'):
            t=t*60
        if v==0:
            s=g*t**2/2
            print('S=',s)
        print('S=',v*t)

        
    if j==('v'):
        s=eval(input('S'))
        k=input('Միավոր')
        t=eval(input('T'))
        p=input('Միավոր')
        if k==('կմ'):
            s=s*1000
        if p==('ժ'):
            t=t*60
        if t==0:
            t= math.sqrt(2*s/g)
        if s==0:
            s=g*t**2/2
        print (s,t)
        print ('V=',s/t)

        
    if j==('t'):
        v=eval(input('V'))
        l=input('Միավոր')
        s=eval(input('S'))
        k=input('Միավոր')
        if l==('կմ/ժ'):
            v=v*3.6
        if k==('կմ'):
            s=s*1000
        if s==0:
            s=g*t**2/2
        if v==0:
            a=input ('a')
            v=a*t
        print ('T=',s/v)
             

