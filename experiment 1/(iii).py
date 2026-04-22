#write a program to illyustrate the use of functions 

def valid_voter(age):
    if age>=18:
        print("the person is eligible for voting ")
    else:
        print("the person is not eligible for voting ")

age=int(input("enter you age in years "))
valid_voter(age)
