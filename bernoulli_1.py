import numpy as np
import matplotlib.pyplot as plt

def tossCoin(p):
    u=np.random.uniform(0,1)
    if u < p:
        return 1
    return 0

def trials_required(k,bias):
    count=0
    cnt=0
    while cnt != k:
        result=tossCoin(bias)
        if result == 1:
           cnt+=1
        count+=1

    return count
       
bias=0.5
k=3
maximum_trials=30
count=np.zeros(maximum_trials)
possible_trials=list(range(0,maximum_trials))
number_of_simulations=10000

for i in range(number_of_simulations):
    n_trials=trials_required(k,bias)
    count[n_trials]+=1

count/=number_of_simulations
plt.bar(possible_trials,count)
plt.xlabel('x')
plt.ylabel('PX(x)')
plt.title('X~Number of trials till kth arrival(k=3,p=0.5)')
plt.show()
