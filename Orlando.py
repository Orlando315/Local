#Orlando Perez 20.336.372

num=int(raw_input("Cuantos elementos va a ingresar?: "))
l=[0]
con=0
while con < num:
    con=con+1
    element=raw_input("Ingrese el elemntento #"+ str(con)+" ")
    l.insert(0,element)
con=1
while con <= num:
    print l[con-1]
    con=con+1

def ordenar_num(l):
    cont=0
    aux=0
    while cont < num:
        if l[cont]< l[con+1]:
            aux=l[cont]
	    l[cont]=l[cont+1]
	    l[cont+1]=aux
	cont=cont+1
