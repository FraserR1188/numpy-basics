#!/usr/bin/env python
# coding: utf-8

# ![Pluralsight Banner](_ignore/stepThree.png)

# ## <font color='130F25'>Task 3.1: Creating an Empty Ndarray<font>

# In[5]:


# Import numpy
import numpy as np
# Create an empty ndarray
array = np.empty((3,3))
print(array)


# ## <font color='130F25'>Task 3.2: Creating a Zeros Ndarray<font>

# In[6]:


# Create a zeros ndarray
zeros = np.zeros((3,3))
print(zeros)


# ## <font color='130F25'>Task 3.3: Creating a Ones Ndarray<font>

# In[7]:


# Create a ones ndarray
ones = np.ones((3,3))
print(ones)


# ## <font color='130F25'>Task 3.4: Creating a Full Ndarray<font>

# In[12]:


# Create a full ndarray

full = np.full((3,3), 7)
print(full)


# ## <font color='130F25'>Task 3.5: Creating an Ndarray from Existing Data<font>

# In[13]:


# Create an ndarray from existing data
list_array = np.asarray([1,2,3,4,5])
print(list_array)


# ## <font color='130F25'>Task 3.6: Creating an Ndarray within a Numerical Range<font>

# In[15]:


# Create an ndarray within a numerical range
numerical_range = np.arange(0,10,2)
print(numerical_range)


# ## <font color='130F25'>Task 3.7: Creating an Ndarray of Evenly Spaced Values<font>

# In[16]:


# Create an ndarray of evenly spaced values
even = np.linspace(5,0,1)
print(even)


# In[ ]:




