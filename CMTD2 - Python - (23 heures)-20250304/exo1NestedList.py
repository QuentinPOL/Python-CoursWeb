a=[1,2,[4,5,6],3]
b=a[:] # avec le b=a[:] on va juste désynchro le contenu du [1]
b.append (4)
b[2].append (7)
print ("a: ", a)
print ("b: ", b)