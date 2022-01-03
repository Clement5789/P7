def facteur(t,t1):
    a = 0
    for i in range(len(t1)):
        while t[i]==t1[i]:
            a = a+1
        if a==len(t):
            return True
        else:
            return False