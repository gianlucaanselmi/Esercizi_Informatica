#Mi riscrivo una funzione che trova il massimo di una lista

def mymax(list):
    m = list[0]
    for n in list:
        if n > m:
            m = n
    return m

# Lista di partenza da ordinare

mylist = [200,7,99,15]

#Lista ordinata, inizialmente vuota

sorted_list = []

# Algoritmo di ordinamento

for idx in range(len(mylist)):
    m = mymax(mylist)
    sorted_list.append(m)
    mylist.remove(m)

    #Stampa della lista appena calcolata
print(sorted_list)



     # Condizioni che devono essere soddisfatte

assert sorted_list[0] == 200
assert sorted_list[1] == 99
assert sorted_list[2] == 15
assert sorted_list[3] == 7