def somme(tab):
    d = 0
    for i in range(len(tab)):
        d = d+tab[i]
    return d

b = 1
i = 0
t = []

def nb_parfaits:
    while True:
        i = i+1
        a = 2**i*(2**(i+1)-1)
        while b<=a/2:
            if a%b==0:
                t.append(b)
                b = b+1
            else:
                b = b+1
        if somme(t)==a:
            print(a)
        d = 0
        t = []
        b = 1