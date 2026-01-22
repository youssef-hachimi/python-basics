# listes on python
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
#print(food[2])
#print(food)

food.append("Tajin")
food.remove("Tajin")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()



for f in food:
    print(f)

# 2D listes = a liste of listes
drinks = ["coffee","atay","milk","soda"]
dinner = ["pizza","hamburger","hotdog",]
dessert = ["cake","ice crem"]

eats = [drinks,dinner,dessert]
#print(eats)
print(eats[0][0]) #coffee
print(eats[0][2]) #milk
print(eats[1][1]) #humburger
print(eats[1][0]) #pizza
print(eats[2][1]) #ice crem

# tuple
student = ("youssef",20,"male","CS")

print(student.count("youssef"))
print(student.index("male"))

for x in student:
    print(x)

if "CS" in student:
    print("he is cybersecurity student")
# Dictionary
capitals = {"USA":'Washington',
            'Morocco':'Rabat',
            'taly':'Milan',
            'China':'Beijing'}
print(capitals['Morocco'])
print(capitals['USA'])
print(capitals['Italy'])
#exercice : 
notes = []

while True:
    note = float(input("Entrez une note entre 1 et 20 (0 pour arrêter) : "))

    if note == 0:
        break

    if 1 <= note <= 20:
        notes.append(note)
    else:
        print("Note invalide, veuillez entrer une note entre 1 et 20.")

# Vérifier s'il y a au moins une note
if len(notes) > 0:
    moyenne = sum(notes) / len(notes)
    note_max = max(notes)
    note_min = min(notes)

    print("\nNombre de notes :", len(notes))
    print("Moyenne :", moyenne)
    print("Note maximale :", note_max)
    print("Note minimale :", note_min)

    # Affichage selon le seuil
    if moyenne >= 12:
        print("Résultat : Validé")
    else:
        print("Résultat : Non validé")
else:
    print("Aucune note saisie.")

#POO in Python
class Personne:
    def __init__(Self,nom,age):
        Self.nom = nom
        Self.age = age
 # create object : 
Personne1 = Personne("youssef",20)
Personne2 = Personne("oumaima",20)
#print 

print(Personne1.nom, Personne1.age)
print(f"HI my name is {Personne2.nom}  and I am {Personne2.age} years old")


# Access Types :
class employee
    def __init__(Self,nom,age,salaire)
        Self.nom = nom # public 
        Self._age = age # protected
        Self.__salaire = alaire #private    
    employee1 = employee("ahmed", 23, 2000)
print(employee1.nom)
print(employee1._age)
print(employee1.__salaire) #error





