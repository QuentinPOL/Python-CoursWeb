import copy
a=[1,2,[4,5,6],3]
b=copy.deepcopy(a) # Utiliser pour la copier d'une liste imbriquée
b.append (4)
b[2].append (7)
print ("a: ", a)
print ("b: ", b)