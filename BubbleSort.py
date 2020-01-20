from timeit import time
from random import randrange

# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(20000)]


# Algoritmo di ordinamento
print("lista prima:")
#print(mylist)
start_time = time.time()

cswap=99
# Scrivere qui l'algoritmo di Bubble Sort
while cswap>0:
    cswap=0
    for idx in range(1,len(mylist)):
        eleswap = 0
        if mylist[idx] < mylist[idx-1]:
            eleswap = mylist[idx]
            mylist[idx] = mylist[idx - 1] 
            mylist[idx-1] = eleswap
            cswap += 1

stop_time = time.time()
print(f"{(stop_time-start_time):.7f}")


# Stampo la lista appena calcolata
print("lista dopo:")
#print(mylist)
