a=int(input("nombre de table à afficher : "))
b=int(input("nombre de multiplicateur : "))
t=0
for i in range(1,a+1):
    print("table de",i)
    for k in range(1,b+1):
        t=i*k
        print(i,"*",k,"=",t)