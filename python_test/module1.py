#coding: utf-8
from PIL import Image
import numpy as np
import scipy as sc
import Cython


def aiueo(a, b):
    c = a + b
    return c

x=4
y=3
t=aiueo(x, y)
print (t)