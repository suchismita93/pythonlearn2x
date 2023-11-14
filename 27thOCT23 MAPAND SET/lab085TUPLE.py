tuple3=tuple(["suchi","Annie"])
print(tuple3)
print(tuple3[1])
print(tuple3[0])
# Merging tuple
hero1=("Ironman","Thor","Spiderman")
hero2=("Hulk","Antman")
avenger_team=hero1 +hero2
print(avenger_team)
#  Convert to list
print(list(avenger_team))

a,b = 23, 45 # This is multiple value assign
q,w,e = (23,45,78) # Tuple assigned to multiple value
print(q)
print(e)
hero1=("Ironman","Thor","Spiderman")
hero2=("Hulk","Antman")
avenger_team2=(hero1 ,hero2) #merge 2tuple  (nestedtuple )
print(avenger_team2)
print(len(avenger_team2))
print(avenger_team2[0])
print(avenger_team2[1])
print(avenger_team2[0][1]) # access the element of the tuple(Thor)
print(avenger_team2[1][0]) # Hulk
print("###",avenger_team2[1][1])

# Search in tuple
Cities=("paris","Londan","india","turkey")
print("paris" in Cities)
print("Japan" in Cities)