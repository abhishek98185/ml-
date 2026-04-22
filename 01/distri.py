import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, expon, binom, poisson
x = np.linspace(0, 10, 100)
plt.figure()
plt.plot(x, uniform(0,10).pdf(x))
plt.title("Uniform PDF")
plt.show()

plt.figure()
plt.plot(x, uniform(0,10).cdf(x))
plt.title("Uniform CDF")
plt.show()

x = np.linspace(-5, 5, 100)
plt.figure()
plt.plot(x, norm(0,1).pdf(x))
plt.title("Normal PDF")
plt.show()

plt.figure()
plt.plot(x, norm(0,1).cdf(x))
plt.title("Normal CDF")
plt.show()

x = np.linspace(0, 5, 100)
plt.figure()
plt.plot(x, expon(scale=1).pdf(x))
plt.title("Exponential PDF")
plt.show()

plt.figure()
plt.plot(x, expon(scale=1).cdf(x))
plt.title("Exponential CDF")
plt.show()

x = np.arange(0,6)
plt.figure()
plt.bar(x, binom(5,0.5).pmf(x))
plt.title("Binomial PMF")
plt.show()

plt.figure()
plt.step(x, binom(5,0.5).cdf(x))
plt.title("Binomial CDF")
plt.show()

x = np.arange(0,10)
plt.figure()
plt.bar(x, poisson(3).pmf(x))
plt.title("Poisson PMF")
plt.show()

plt.figure()
plt.step(x, poisson(3).cdf(x))
plt.title("Poisson CDF")
plt.show()