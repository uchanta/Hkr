#!/usr/bin/env python
# coding: utf-8

# HASHLIB: How to used HASHLIB.
# @ucz

# In[8]:


import hashlib


# In[11]:


h = hashlib.new("sha1", b"cadena")


# In[12]:


print(h.digest)


# DIGEST method: It is the code in binary

# In[18]:


h.digest()


# HEXADIGEST method: It is the code in exadecimaly.

# In[13]:


print(h.hexdigest())


# In[14]:


m = hashlib.sha1()


# In[15]:


m.update(b"cadena")


# In[16]:


m.digest()


# In[17]:


m.hexdigest()


# In[ ]:




