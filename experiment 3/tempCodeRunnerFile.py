import matplotlib.pyplot as plt 
import seaborn as sn 
values=[[101,5,7,],[113,17,19],[123,29,31]]
sn.heatmap(data=values,annot=True,fmt="d")
plt.show()