def append(number, number_list=None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    print(number_list)
    return number_list

append(5)
append(7) 

#Q6 Il y a bien que un seul chiffre dans le tableau
#Q7 number_list=None un seul chiffre dans le tableau et 
#number_list=[] bah tout les chiffres qui seront appeler dans la fonction