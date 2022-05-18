import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(27).reshape(3,3,3)


# plt.plot(hist)
# plt.show()
# print(arr)
# print("  ")
sum = (np.sum(arr,axis = 1))

# for i in range(3):
#     for j in range(3):
#         for k in range(3):
result = []
for i in arr:

    temp = i/sum
    result.append(temp)
    

final_result = np.array(result)
print(final_result)
print(final_result.shape)
print(type(final_result))