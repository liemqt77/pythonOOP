from difflib import ndiff

import  numpy as np
"""
arr = np.array(20) 
print(arr)#0Dimension
"""

"""
arr = np.array([1,2,3,4,5])
print(arr) #1Dimension
"""


"""
arr = np.array([[1,2,3], [4,5,6]])
print(arr) #2Dimension
"""

"""
arr = np.array([[1,2,3], [4,5,6], [7,8,9]] )
print(arr) #3Dimension
"""

"""
a = np.array(10)
b = np.array([1,2,3])
c = np.array([[4,5,6], [7,8,9]])
d = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
"""


arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print('number of dimension: ', arr.ndim)