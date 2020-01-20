from timeit import time
from random import randrange

# Mi riscrivo una funzione che trova il minimo di una lista
def mymin(list):
    m_idx = 0
    m = list[0]
    for n_idx, n in enumerate(list):
        if n < m:
            m = n
            m_idx = n_idx
    return m, m_idx

# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(50000)]

# Algoritmo di ordinamento
#print("lista prima:")
#print(mylist)
start_time = time.time()

for idx in range(len(mylist)):
    # compute minimum and the index relative to the slice
    m, m_idx = mymin(mylist[idx::])
    # convert relative index into global index
    m_idx += idx
    swap = mylist[idx]
    mylist[idx] = m
    mylist[m_idx] = swap
    
print("Ordinamento completo")
stop_time = time.time()
print(f"{(stop_time-start_time):.7f}")


# Stampo la lista appena calcolata
#print("lista dopo:")
#print(mylist)

assert mylist==sorted(mylist)
