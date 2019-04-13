import matplotlib.pyplot as plt

data = [301205,60169,15670,6423,3740,2655,2143,1912,1776,1690,1610,1520,1477,1458,1449,1424,1414,1407,1400,1392]
data2 = [278482,29438,5769,2692,1901,1568,1395,1305,1251,1210,1183,1168,1155,1151,1145,1138,1133]
fig1, ax1 = plt.subplots()
plt.plot(data)
#plt.plot(data2)
plt.yscale('log')
plt.title('Cluster found in each iteration')
plt.grid(True)
plt.yticks([1000,5000,10000,50000,100000,500000])

plt.xticks(range(0,20))
plt.xlabel('Iterations')
plt.ylabel('Clusters')

plt.show()