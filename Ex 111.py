def somme_produits(t1,t2):
    somme=0
    for a in t1:
        for b in t2:
            somme=somme+a*b
    return somme

def produit_sommes(t1,t2):
    somme1=0
    somme2=0
    for a in t1:
        somme1=sommme1+a
    for b in t2:
        somme2=somme2+b
    return somme1*somme2