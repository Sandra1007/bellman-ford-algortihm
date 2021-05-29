#bellman ford: ide po redu , djikstra trazi najmaji

from curkovic_sandra_dijkstra import CitajFile
from curkovic_sandra_dijkstra import PretvoriUint
import time
rjecnik ={
    0:0,
    1:10000,
    2:10000,
    3:10000,
    4:10000,
    5:10000,
    6:10000,
    7:10000,
    8:10000,
    9:10000,
    10:10000,
 
}

def Bellman_Ford(integeri,brojac):
    
    preskoci=True
    je_li_do_kraja=0 #provjeri jesmo li dosli do kraja petlje da se resetira
    koliko_iteracija=0 #broj vrhova minus 1
    while(preskoci):
        preskoci=False
        for x in integeri[1:]:
            if(rjecnik[x[0]]+x[2]<rjecnik[x[1]]): #npr. [3,2,-10] => rjecnik[3]+(-10)<rjecnik[2]
                rjecnik[x[1]]=rjecnik[x[0]]+x[2]
            je_li_do_kraja=je_li_do_kraja+1

        if(je_li_do_kraja==brojac-1): #brojac -1 jer broji i arcs pa jedna lista je viska
            je_li_do_kraja=0 #resetiraj ga ako smo do kraja
            preskoci=True
            koliko_iteracija=koliko_iteracija+1

        if(koliko_iteracija==10): #koliko je vrhova -1
            break
            
    
    print(rjecnik)


start=time.time() 
lista_u_listi, brojac=CitajFile()
integeri=PretvoriUint(lista_u_listi)

Bellman_Ford(integeri,brojac)
print(time.time()-start)