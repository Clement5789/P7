def crible(N):
    z = 0
    t = [True]*N
    t[0] = False
    t[1] = False
    for i in range(len(t)):
        a = 2
        if t[i]==True:
            z = z+1
            while i*a<len(t):
                t[i*a] = False
                a = a+1
        else:
            continue
    print(t,z)