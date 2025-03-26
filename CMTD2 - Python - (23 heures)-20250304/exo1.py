a=[1,2,3]
b=a[:] # b=a veut dire on copie comme un objet contrairement à b=a[:]
b.append(4)
print("a: ", a)
print("b: ", b)
#Utiliser pour la copie de liste normale
