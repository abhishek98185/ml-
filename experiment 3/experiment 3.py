# import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7,8]
# y=[2,4,6,8,10,12,14,16]
# plt.plot(x,y)
# plt.show()



# # linegraph 

# import matplotlib.pyplot as plt 
# x=[12,13,15,20,25,33,34,36,43]
# y=[43,23,65,34,98,23,84,15,67]

# plt.plot(x,y)
# plt.title("line graph")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()


#multiple line graph 

# import matplotlib.pyplot as plt

# x  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y1 = [12, 18, 25, 30, 28, 45, 52, 60, 68, 75]
# y2 = [8, 14, 30, 37, 33, 40, 46, 53, 59, 65]
# y3 = [5, 10, 15, 21, 36, 32, 37, 43, 48, 54]
# plt.plot(x,y1,color="red")
# plt.plot(x,y2,color="blue")
# plt.plot(x,y3,color="green")
# plt.title("multiple line graph ")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

#multiline graph bt change theme


# import matplotlib.pyplot as plt


# x  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y1 = [12, 18, 25, 30, 28, 45, 52, 60, 68, 75]
# y2 = [8, 14, 30, 37, 33, 40, 46, 53, 59, 65]
# y3 = [5, 10, 15, 21, 36, 32, 37, 43, 48, 54]
# plt.plot(x,y1,color="red",label="line 1")
# plt.plot(x,y2,color="blue",label="line 2")
# plt.plot(x,y3,color="green",label="line 3")
# plt.title("multiple line graph ")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()
# plt.show()


#bargraph 

# import matplotlib.pyplot as plt 

# x=[2,4,6,8,10,12,14,16,18,20]
# y=[13,45,23,56,22,35,22,35,23,52]
# plt.bar(x,y,color="cyan")
# plt.title("bargraph")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()


#horizontal bargraph 

# import matplotlib.pyplot as plt 

# x=[1,2,3,4,5,6,7,8,9,10]
# y=[12,34,23,53,23,52,21,23,12,34]
# plt.barh(x,y,color="magenta")
# plt.title("horizontal bar graph ")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()


#handling huge variation using log scale 

# import matplotlib.pyplot as plt 


# # before log scale 

# x=[1,2,3,4,5,6,7,8,9,10]
# y=[1023,101,234,7,11,10023,3421,10001,34,2]
# plt.bar(x,y,color="green")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()


# # after using log scale 

# plt.bar(x,y,color="green")
# plt.yscale("log")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()






# heat map 
# import matplotlib.pyplot as plt 
# import seaborn as sn 
# values=[[0,10,20],[30,40,50],[60,70,80]]
# sn.heatmap(data=values)
# plt.show()


#add attonations to heatmap

# import matplotlib.pyplot as plt 
# import seaborn as sn 
# values=[[101,5,7,],[113,17,19],[123,29,31]]
# sn.heatmap(data=values,annot=True)
# plt.show()


#changing from scientific notation to integer 



# import matplotlib.pyplot as plt 
# import seaborn as sn 
# values=[[101,5,7,],[113,17,19],[123,29,31]]
# sn.heatmap(data=values,annot=True,fmt="d")
# plt.show()



#using set labels 

import matplotlib.pyplot as plt 
import seaborn as sn
values=[[133,234,234],[123,234,212],[342,214,234]]
title="Heatmap"
xlabel=["A","B","C"]
ylabel=[1,2,3]
hm=sn.heatmap(data=values , annot=True,fmt="d",xticklabels=xlabel,yticklabels=ylabel)
hm.set(title=title,xlabel="x-axis",ylabel="y-axis")
plt.show()
