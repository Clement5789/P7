def nb_triplets(bs):
    if bs>200:
        print("Le programme est trop complexe")
    else:
        nb = 0
        for a in range(1,bs+1):
            for b in range(a,bs+1):
                for c in range(b,bs+1):
                    if a**2+b**2==c**2:
                        print(a,b,c)
                        nb = nb+1
        return nb