#!/usr/bin/env python
# coding: utf-8

# # Elaboración de la libreria de Números Complejos 

# A lo largo de este documento vamos a escribir funciones que nos permiten trabajar con números complejos

# # Representación de un número complejo

# El número $a + bi$ lo representaremos mediante la lista: [a, b]

# A continuación definiremos una función para la suma de 2 números complejos:

# In[4]:


def suma(c_1, c_2):
    """
    La función suma recibe dos números complejos c_1 y c_2 (que deben ser listas de longitud 2)
    y retorna un complejo (lista de longitud 2) correspondiente a la operación c_1 + c_2.
    """
    return [c_1[0] + c_2[0], c_1[1] + c_2[1]]


# Probemos la función `suma`

# In[2]:


c_1 = [3,2]
c_2 = [7,5]
suma(c_1, c_2)


# Justificación de la prueba:
# $$(3 + 2i) + (7 + 5i) = (3 + 7) + (2 + 5)i = 10 + 7i$$

# A continuación definiremos una función para la resta de 2 números complejos:

# In[16]:


def resta(c_1, c_2):
    """
    La función resta recibe dos números complejos c_1 y c_2 (que deben ser listas de longitud 2)
    y retorna un complejo (lista de longitud 2) correspondiente a la operación c_1 - c_2.
    """
    return [c_1[0] - c_2[0], c_1[1] - c_2[1]]


# Probemos la función `resta`

# In[17]:


c_1 = [3,2]
c_2 = [7,5]
resta(c_1, c_2)


# Justificación de la prueba:
# $$(3 + 2i) - (7 + 5i) = (3 - 7) + (2 - 5)i = -4 + (-3i)$$

# A continuación definiremos la función para la multiplicación de 2 números complejos:

# In[18]:


def producto(c_1, c_2):
    """
    La función producto recibe dos números complejos c_1 y c_2 (que deben ser listas de longitud 2)
    y retorna un complejo (lista de longitud 2) correspondiente a la operación c_1 * c_2.
    """
    return [(c_1[0] * c_2[0]) - (c_1[1] * c_2[1]), (c_1[0] * c_2[1]) + (c_1[1] * c_2[0])]


# Probemos la función `producto`

# In[19]:


c_1 = [3,2]
c_2 = [7,5]
producto(c_1, c_2)


# Justificación de la prueba:
# $$(3 + 2i) * (7 + 5i) = (3 * 7) + (3 * 5)i + (2 * 7)i - (2 * 5) = 11 + 29i$$

# A continuación definiremos la función para la conjugación de un número:

# In[20]:


def conjugado(c_1):
    """
    La función conjugado recibe un número complejo (lista de longitud 2) y retorna un complejo
    (lista de longitud 2) correspondiente a la operación a - bi.
    """
    return [c_1[0], -(c_1[1])]


# Probemos la función `conjugado`

# In[21]:


c_1 = [3,2]
conjugado(c_1)


# Justificación de la prueba:
# $$(3 + 2i) = 3 - 2i$$

# A continuación definiremos la función para la división de dos números complejos:

# In[22]:


def division(c_1, c_2):
    """
    La función division recibe dos números complejos c_1 y c_2 (que deben ser listas de longitud 2)
    y retorna un complejo (lista de longitud 2) correspondiente a la operación c_1 / c_2.
    """
    n_c = conjugado(c_2)
    mul_1 = producto(c_1, n_c)
    mul_2 = produnto(c_2, n_c)
    return [mul_1 / mul_2]


# Probemos la función `división`

# In[31]:


c_1 = [3,2]
c_2 = [7,5]
division(c_1, c_2)


# A continuación definiremos la función modulo de un número complejo:

# In[23]:


def modulo(c_1):
    """
    La función modulo recibe un número complejo (lista de longitud 2) y retorna un número flotante
    correspondiente a la operación (a**2 + b**2)**(1/2).
    """
    return [(c_1[0]**2 + c_1[1]**2)**(1/2)]


# Probamos la función `modulo`

# In[24]:


c_1 = [3,2]
modulo(c_1)


# Justificación de la prueba
# $$|(3 + 2i)| = (3**2 + 2**2)**(1/2) = (9 + 4)**(1/2) = 13**(1/2) = 3.60$$

# A continuación definiremos la función cartesiana_polar:

# In[27]:


def cartesiana_polar(c_1):
    """
    La función cartesiana_polar recibe un número complejo (lista de longitud dos) que se encuentra en coordenadas
    cartesianas y retorna un complejo (lista de longitud 2) que esta en coordenda polar.
    """
    ang = arctan ((c_1[1])/(c_1[0]))
    mod = modulo(c_1)
    return [mod, ang]


# Probamos la función `cartesiana_polar`

# In[28]:


c_1 = [3,2]
cartesiana_polar(c_1)


# Justificación de la prueba
# $$$$
