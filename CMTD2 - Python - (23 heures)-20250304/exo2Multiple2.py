def multipleByTwo(maliste: list):
    return list(map(lambda x: 2*x, maliste))

#Q1 map va prendre chaque élément d'un iterable et lui appliquer une fonction
#Q2 lambda =  fonction anonyme plus simple
#Q3 return [2 * x for x in maliste]
#Q4 Aucun changement lors du rajout de la ligne, bah oui c'est conforme

lst = [1, 2, 3, 9, 8, 7]
print(multipleByTwo(lst))
print(multipleByTwo(lst))