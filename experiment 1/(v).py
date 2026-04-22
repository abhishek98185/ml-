#Write a program to perfom the various string operations 

name="Abhishek  Singh"
length=len(name)
print("the length of string is ",length)

#checking if is upper 
print("are all letter in upper case? ", name.isupper())

#checking if lower 
print("are all letter in lower case? ",name.islower())

# replace double space by single
print("replacing double space with single ", name.replace("  "," "))

#getting index of i 
print("returning index of first occuring i ", name.index("i"))
#getting index of rightmost i 
print("returning index of last occuring ", name.rfind("i"))

print("the capitalised form ",name.capitalize())
print("upper case form ",name.upper())
print("lower case form ",name.lower())