import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#pip install (package name)

#np is array for more complex mathmatical functions
#pd is more for data analysis

x = np.array([1,2,3,4,5])
print(x)
print(x*5)
#multiplies each value in np array by 5
#instead of printing array 5 times

data = pd.read_csv('data.csv')
print(data)
#imports csv in same location as .py file
ids = data['id']

animals = data['speciesname']
for i in range(100):
    print(ids[i])
plt.figure()
plt.title('Animal IDs')
plt.plot(range(len(ids)), ids, 'rx')

#rx plots as red with x as points
plt.show()


x = ['a','b','c']
y = [1,10,100]

plt.figure()
plt.subplot(1,3,1)
plt.bar(x,y)
plt.subplot(1,3,2)
plt.scatter(x,y)
plt.subplot(1,3,3)
plt.plot(x,y)
plt.suptitle('Types of plotting')
plt.show()

plt.figure(figsize=(15,3))
plt.hist(animals)
plt.show()
#makes a line graph index(x) vs value(y)

