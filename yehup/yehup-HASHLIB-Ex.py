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


# HEXADIGEST method: It is the code in exadecimaly

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


# In[19]:


u = hashlib.sha1()


# In[20]:


u.update(b"www.recursospython.com ")
u.update(b"- Recursos Python")
print(u.digest(), u.hexdigest())


# La colección hashlib.algorithms_guaranteed provee los nombres de los algoritmos soportados por el módulo

# In[21]:


for algorithm in hashlib.algorithms_guaranteed:
    print(algorithm)
    h = hashlib.new(algorithm)
    h.update(b"www.recursospython.com - Recursos Python")
    try:
        print(h.hexdigest())
    except TypeError:
        # Algoritmo SHAKE requiere la longitud como argumento.
        print(h.hexdigest(128))


# Ejemplos
# El siguiente script imprime el hash correspondiente para cada uno de los archivos contenidos en la carpeta en donde se encuentra ubicado, aplicando los distintos algoritmos que presenta hashlib.

# In[22]:


import hashlib
from os import listdir
from os.path import isdir, islink
for filename in listdir("."):
    if not isdir(filename) and not islink(filename):
        try:
            f = open(filename, "rb")
        except IOError as e:
            print(e)
        else:
            data = f.read()
            f.close()
            print("** %s **" % filename)
            for algorithm in hashlib.algorithms_guaranteed:
                h = hashlib.new(algorithm)
                h.update(data)
                try:
                    hexdigest = h.hexdigest()
                except TypeError:
                    hexdigest = h.hexdigest(128)
                print("%s: %s" % (algorithm, hexdigest))
            print()

