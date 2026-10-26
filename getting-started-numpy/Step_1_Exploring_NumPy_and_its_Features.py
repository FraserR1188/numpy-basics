#!/usr/bin/env python
# coding: utf-8

# ![Pluralsight Banner](_ignore/stepOne.png)

# ## <font color='130F25'>Task 1.1: Creating a NumPy Array<font>

# In[1]:


import numpy as np

# Create and print a numpy array with integers from 1 to 10
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(data)


# ## <font color='130F25'>Task 1.2: Performing Basic Operations<font>

# In[4]:


# Perform addition, subtraction, multiplication, and division on the array

print(data + 10)
print(data - 5)
print(data * 3)
print(data / 2)


# ## <font color='130F25'>Task 1.3: Comparing Performance with Python Lists<font>

# In[5]:


import time

# Create a Python list with integers from 1 to 1 000 000
oneMillion = [num for num in range(1, int(1e6)+1)]

# Time the execution of addition operation on the list
start_time = time.time()
list = [i + 10 for i in oneMillion]
end_time = time.time()

# Print the execution time
print('Execution time for list (seconds): ', end_time - start_time)

# Create the array
array = np.array(oneMillion)

# Time the execution of addition operation on the array
start_time = time.time()
array = array + 10
end_time = time.time()

# Print the execution time
print('Execution time for array (seconds): ', end_time - start_time)


# ###### <font color='130F25'>To go to the next step, click on the orange jupyter logo at the top of the editor.</font>
