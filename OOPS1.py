class Parent(object):
    pass
class Child(Parent):
    pass

#Driver Code
print(issubclass(Child,Parent))
print(issubclass(Parent,Child))

obj1= Child()
obj2=Parent()

print(isinstance(obj2, Child))
print(isinstance(obj2, Parent))

def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper
@splitter_decorator
@lowercase_decorator
def hello():
    return 'Hello world'
hello()


temp = 10
def func():
    temp = 20
    print(temp)
print(temp)
func()
print(temp)

temp = 10
def func():
    global temp
    temp = 20
    print(temp)
print(temp)
func()
print(temp)

mul = lambda a,b: a*b
print(mul(2,5))

def myWrapper(n):
    return lambda a:a*n
mulFive = myWrapper(5)
print(mulFive(2))

arr = [1,2,3,4,5,6]
print(arr[-1])
print(arr[-2])

def multiply(a,b,*argv):
    mul = a * b
    for num in argv:
        mul *=num
    return mul
print(multiply(1,2,3,4,5))

def appendNumber(arr):
    arr.append(4)
arr = [1,2,3]
print(arr)
appendNumber(arr)
print(arr)


import pandas as pd
import numpy as np

df1 = pd.Series([2,4,5,8,10])
df2 = pd.Series([8,10,13,15,17])

p_union = pd.Series(np.union1d(df1,df2))
p_interect = pd.Series(np.intersect1d(df1,df2))
unique_elements = p_union[~p_union.isin(p_interect)]
print(unique_elements)

import pandas as pd
dict_info = {'key1' : 2.0,'key2':3.1,'key3':2.2}
series_obj = pd.Series(dict_info)
print(series_obj)

reversed_array = arr[::-1]

import numpy as np
def find_nearest_value(arr,value):
    arr = np.asarray(arr)
    idx = (np.abs(arr-value)).argmin()
    return arr[idx]
arr = np.array([0.21169, 0.61391, 0.6341,0.0131,0.16541,0.5645,0.5742])
value = 0.52
print (find_nearest_value(arr,value))


x = lambda a : a+10
print(x(5))