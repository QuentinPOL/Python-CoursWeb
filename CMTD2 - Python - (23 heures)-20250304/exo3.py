#encoding:utf-8
from pick import pick
import pandas as pd
from statistics import mean

read_file = pd.read_excel (r'Classeur_notes_exemple.xlsx', sheet_name='Feuil1')
read_file.to_csv (r'Classeur_notes_exemple.csv', index = None, header=True)

df = pd.read_csv(r'Classeur_notes_exemple.csv')
notes_brutes = df['Note brute'].values.tolist()

min_mark = min(notes_brutes)
max_mark = max(notes_brutes)
delta_mark = max_mark - min_mark

### Atteinte d'une moyenne précise
wanted_avg_mark = 9.0

avg_mark = mean(notes_brutes)
diff_avg = wanted_avg_mark - avg_mark

notes = df['Note brute'].apply(lambda x: x + diff_avg)
if notes.max() > 20:
    notes = notes.apply(lambda x: x - (notes.max()-20) ) 

    y = 0
    delta = 1
    dir = "up"
    y_max = notes.max()
    y_min = notes.min()
    while True:
        _notes = notes.apply(lambda x: round((y_max - (y_min + y))/delta_mark*(x-max_mark) + 20, 2) )
        actual_diff_avg = wanted_avg_mark - _notes.mean()
        if actual_diff_avg > 0.001:
            if dir == "down":
                delta /= 2
            y += delta
            dir = "up"
        elif actual_diff_avg < -0.001:
            if dir == "up":
                delta /= 2
            y -= delta
            dir = "down"
        else: 
            notes = _notes
            break

print(notes.apply(lambda x: round(x,2)))
print(notes.mean())

df["Note recalibrée"] = notes
print(df)

df = df.reset_index(drop=True)
try:
    with pd.ExcelWriter(r'Classeur_notes_exemple.xlsx', engine="openpyxl", mode='a') as writer:  
        df.to_excel(writer, sheet_name='Feuil2')  
except (PermissionError):
    print("Veuillez fermer le fichier svp.")
except (ValueError):
    print("L'onglet demandé existe déjà.")


#Q1 atteindre une moyenne précise donnée (ici 9.0), tout en respectant une limite maximale de 20
#Q2 1. Lecture du fichier excel, 2. Convertion en fichier csv
#3. Notre brutes récupérer dans Note brute et converti en liste
#4. Détermination de la note min, max, et du delta écart max-min.
#5 Calcul de la moyenne actuelle et de l’écart avec la moyenne désirée.
#6 Toutes les notes sont augmentées/diminuées pour ajuster la moyenne.
#Si des notes dépassent 20 on ajuste.
#7. Une boucle ajuste les notes de façon plus jsp pour que la moyenne soit atteinte sans dépasser 20.
#8. Utilisation d’une transformation linéaire (ressemble à une normalisation inversée).
#9. Les notes recalibrées sont affichées avec la moyenne.
#10. Les notes recalibrées sont ajoutées dans une nouvelle feuille du fichier Excel.
#11. Gestion des erreurs d’écriture : si le fichier est ouvert ou si l’onglet existe déjà.
#Q3 Permet gérer les erreurs et de les remmontés pour savoir ce qu'il ce passe 
#Q4
#Q5
#Q6
#Q7