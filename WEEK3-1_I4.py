arr = [23, 25, 30, 1, 10, 18]
print("Element at index 0:", arr[0])
print("Element at index 3:", arr[3])
print("Last element:", arr[-1])
print("Elements from index 1 to 4:", arr[1:5])
print("First three elements:", arr[:3])
print("Elements from index 2 :", arr[2:])
arr[2] = 35
print("Modified array:", arr)
import numpy as np
npa=np.array(arr)
print("sum of elements : ",np.sum(npa))
print("maximum element in the array : ",np.max(arr))
print("minimum element in the array : ",np.min(arr))
print("average of elements in the array : ",np.mean(arr))
print("standard deviation of elements in the array : ",np.std(arr))
print("after multiplying with 3 with the array elements : ",arr*3)