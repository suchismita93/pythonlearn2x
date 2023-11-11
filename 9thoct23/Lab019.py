name="suchi"
#String function
#pyhton string immutable in nature-They can;t chnge
print(name)
result=name.capitalize() #capital letter
print(result)
result2=name.upper() #upper case
print(result2)
print(id(name))
print(id(result))
print(id(result2 ))
result3=name.lower() #lower case
print(result3)
print(id(result3))

#swapcase()
#returs a copy of the string with upercase cha to lower case
#vice versa
name="suchismita"
print(name.swapcase())

#title
#retuns a title cased version of the string
#where words start with an uppervcase char and
#the remaining char are lower case
name5="python course"
print(name5.title())
print(len(name5))

#replace
text="hello pythonx"
res=text.replace("python","world")
print(res)

#find()
#returns the lower index of a substring inthe string
#returns -1 f the subssrting is not found
text1="hello world"
index=text.find("world")
print(index)
#print(text1[6])

#count()
count=text1.count("o")
print(count)
count2=name.count("z")
print(count2)
ind=name.find("chi")
print(ind)
ln= len(name5)
print(ln)
