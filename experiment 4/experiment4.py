#To implement continious and discrete probablity density function and cummulative distribution function in python using scipy library

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, expon, binom , poisson 
def plotdistribution(dist,x,title):
    pdf=dist.pdf(x)
    cdf=dist.cdf(x)

    plt.figure(figsize=(8,4))

    plt.subplot(1,2,1)
    plt.plot(x,pdf,'r-',lw=2)
    plt.title(f"PDF of {title}")
    plt.xlabel("x")
    plt.ylabel("Probability density")

    plt.subplot(1,2,2)
    plt.plot(x,cdf,'b-',lw=2)
    plt.title(f"CDF of {title}")
    plt.xlabel("x")
    plt.ylabel("Cumulative Probability ")

    plt.tight_layout(pad=5.0)
    plt.show()


#1. Uniform distribution
a,b=0,10   #start and end of uniform distribution
x_uniform=np.linspace(a,b,100)
uniform_dist=uniform(a,b-a)
plotdistribution(uniform_dist,x_uniform,"uniform distribution")



#2 Normal distribution 
mean,std=0,1
x_norm=np.linspace(-5,5,100)
normal_dist=norm(mean,std)
plotdistribution(normal_dist,x_norm,"Normal Distribution")



#3.Exponential distribution 

scale=1
x_exp=np.linspace(0,10,100)
exponential_dist=expon(scale=scale)
plotdistribution(exponential_dist,x_exp,"exponential distribution")




#binomial (discrete )
n,p=10,0.5  #number of trials and probability of success
x_binom=np.arange(0,n+1)
binom_dist=binom(n,p)

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.bar(x_binom,binom_dist.pmf(x_binom),color="r")
plt.xlabel("Number of Success")
plt.ylabel("Probability")
plt.title("PMF for binomial distribution ")


plt.subplot(1,2,2)
plt.step(x_binom,binom_dist.cdf(x_binom),color="b")
plt.xlabel("Number of Success")
plt.ylabel("Cummulative Probability")
plt.title("CDF for binomial distribution")
plt.tight_layout(pad=5.0)
plt.show()




#5.Possion Distribution

lambda_poisson=4  # mean number of even 
x_poisson=np.arange(0,15)
poisson_dist=poisson(lambda_poisson)

plt.subplot(1,3,1)
plt.bar(x_poisson,poisson_dist.pmf(x_poisson),color="red")


plt.subplot(1,3,2)
plt.step(x_poisson,poisson_dist.cdf(x_poisson),color="blue")
plt.subplot(1,3,3)
plt.step(x_poisson,poisson_dist.cdf(x_poisson),color="green")


plt.show()