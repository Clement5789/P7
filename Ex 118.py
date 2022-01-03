def inclus(tab1,tab2):
    a = 0
    for i in range(len(tab1)):
        for j in range(len(tab2)):
            if tab1[i]==tab2[j]:
                a = a+1
                break
            else:
                continue
    if a==len(tab1):
        return True
    else:
        return False