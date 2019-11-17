#!/usr/bin/env python
# coding: utf-8

# HASHLIB: How to used HASHLIB.
# @ucz

import hashlib

h = hashlib.new("sha1", b"cadena")

print(h.digest)

# DIGEST method: It is the code in binary

h.digest()

# HEXADIGEST method: It is the code in exadecimaly.

print(h.hexdigest())

m = hashlib.sha1()

m.update(b"cadena")

m.digest()

m.hexdigest()
