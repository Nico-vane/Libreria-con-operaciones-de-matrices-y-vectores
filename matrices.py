import complejos as com
import math

def suma_m(m_1,m_2):
    """"""
    if (len(m_1) == len(m_2)) and (len(m_1[0]) == len(m_2[0])):
        matriz = []
        for i in range (len(m_1)):
            filas = []
            for j in range(len(m_1[0])):
                matriz.append(com.suma(m_1[i][j], m_2[i][j]))
            matriz.append(filas)
        return matriz

    else:
        print("Las matrices no se pueden operar")

def suma_v(v_1,v_2):
    """"""
    if len(v_1) == len(v_2):
        res = []
        for i in range(len(v_1)):
           res.append(com.suma(v_1[i],v_2[i]))
           print(res)
    else:
        print("Los vectores no se pueden operar")

def inverso_v(v_1):
    """"""
    vector = []
    for i in range (len(v_1)):
        vector.append(v_1[i][0]*(-1),v_1[i][1]*(-1))
    return resp

def mul_e_v(a,v_1):
    """"""
    respt = []
    for i in range (len(v_1)):
        respt.append(com.producto(a,v_1[i]))
    return respt

def multiplicacion_m(m_1,m_2):
    """"""
    if (len(m_1[0]) == len(m_2)):
        for i in range (len(m_1)):
            for j in range (len(m_2[0])):
                for k in range (len(m_1[0])):
                    matriz[i][j] = com.suma(matriz[i][j],com.producto(m_1[i][k],m_2[k][j]))
        return matriz
    else:
        print("No se pueden multiplicar")

def inversa_m(m_1):
    """"""
    matriz = []
    for i in range(len(m_1)):
        filas = []
        for j in range (len(m_1[0])):
            filas.append(m_1[i][j][0]*(-1),m_1[i][j][1]*(-1))
        matriz.append(filas)
    return filas

def mul_e_m(a,m_1):
    """"""
    matriz = []
    for i in range(len(m_1)):
        filas = []
        for j in range(len(m_1[0])):
            filas.append(com.producto(a,m_1[i][j]))
        matriz.append(filas)
    return matriz

def transpuesta(e_1):
    """"""
    matriz = []
    for i in range(len(e_1)):
        filas = []
        for j in range(len(e_1[0])):
            filas.append(e_1[j][i])
        matriz.append(filas)
    return matriz

def conjugada(e_1):
    """"""
    matriz = []
    for i in range(len(e_1)):
        filas = []
        for j in range(len(e_1[0])):
            filas.append(com.conjugada(e_1[i][j]))
        matriz.append(filas)
    return matriz

def adjunta(e_1):
    """"""
    c_1 = conjugada(e_1)
    t_e = transpuesta(c_1)
    return t_e

def accion_m_v(m_1,v_1):
    """"""
    if len(e_1[0]) == 1:
        res = multiplicacion_m(m_1,v_1)
        return res
    else:
        print("No se pueden multiplicar")

def m_compatibles(m_1,m_2):
    """"""
    if len(m_1) == len(m_2[0]):
        m_m = multiplicacion_m(m_1,m_2)
        return m_m
    else:
        print("No son compatibles")

def p_interno(v_1,v_2):
    """"""
    daga = adjunta(v_1)
    total = multiplicacion_m(daga,v_2)
    return total

def norma(v_1):
    """"""
    d_v = adjunta(v_1)
    mul = multiplicacion_m(d_v,v_1)
    return math.sqrt(mul)

def distancia(v_1,v_2):
    """"""
    vector = []
    if len(v_1) == len(v_2):
        for i in range (len(v_1)):
            vector.append(com.resta(v_1[i],v_2[i]))
    return norma(vector)

def m_unitaria(m_1):
    """"""
    if len(m_1) == len(m_1[0]):
        d_m = adjunta(m_1)
        multi = multiplicacion_m(m_1,daga)
        for i in range(len(m_1)):
            for j in range(len(m_1)):
                if (i == j) and (multi[i][j] == 1):
                    print("La matriz es unitaria")
    else:
        print("La matriz no es unitaria")

def m_hermitiana(m_1):
    """"""
    dag = adjunta(m_1)
    for i in range(len(m_1)):
        for j in range(len(m_1[0])):
            if m_1[i][j] == dag[i][j]:
                print("La matriz es Hermitiana")
            else:
                print("La matriz no es Hermitiana")

def p_tensorial(m_1,m_2):
    """"""
    matriz = []
    for i in range(len(m_1)):
        for j in range(len(m_1[0])):
            esca = m_1[i][j]
            matriz.append(mul_e_m(esca,m_2))
    return matriz
