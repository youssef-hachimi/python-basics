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






