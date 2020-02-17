import matrices as m
import math
def test_suma_m():
    assert m.suma_m([[[2,3],[5,-2]],[[1,4],[1,-1]]], [[[3,4],[4,5]],[[2,-1],[3,-2]]]) == [[[5,7],[9,3]],[[3,3],[4,-3]]]

def test_suma_v():
    assert m.suma_v([[[2,3]],[[1,4]]], [[[5,-2]],[[1,-1]]]) == [[[7,1]],[[2,3]]]

def test_inverso_v():
    assert m.inverso_v([[[2,3]],[[1,4]],[[5,-2]]]) == [[[-2,-3]],[[-1,-4]],[[-5,2]]]

def test_mul_e_v():
    assert m.mul_e_v(4,[[[2,3]],[[1,4]]]) == [[[8,12]],[[4,16]]]

def test_multiplicacion_m():
    assert m.multiplicacion_m([[[2,3],[5,-2]],[[1,4],[1,-1]]], [[[3,4],[4,5]],[[2,-1],[3,-2]]]) == [[[2,8],[4,6]],[[-12,13],[-15,16]]]

def test_inversa_m():
    assert m.inversa_m([[[3,4],[4,5]],[[2,-1],[3,-2]]]) == [[[-3,-4],[-4,-5]],[[-2,1],[-3,2]]]

def test_mul_e_v():
    assert m.mul_e_m(2,([[[3,4],[4,5]],[[2,-1],[3,-2]]])) == [[[6,8],[8,10]],[[4,-2],[6,-4]]]

def test_transpuesta():
    assert m.transpuesta([[[2,3],[3,4]],[[1,4],[2,-1]],[[1,-1],[5,-2]]]) == [[[2,3],[1,4],[1,-1]],[[3,4],[2,-1],[5,-2]]]

def test_conjugada():
    assert m.conjugada([[[2,3],[3,4]],[[1,4],[2,-1]],[[1,-1],[5,-2]]]) == [[[2,-3],[3,-4]],[[1,-4],[2,1]],[[1,1],[5,2]]]

def test_adjunta():
    assert m.adjunta([[[2,3],[3,4]],[[1,4],[2,-1]],[[1,-1],[5,-2]]]) == [[[2,-3],[1,-4],[1,1]],[[3,-4],[2,1],[5,2]]]

def test_accion_m_v():
    assert m.accion_m_v([[[2,3],[3,4]],[[1,4],[2,-1]]],[[[1,-1]],[[5,-2]]]) == [[[28,15]],[[13,-6]]]

def test_m_compatibles():
    assert m.m_compatibles([[[2,3],[5,-4]],[[1,2],[1,-1]]],[[[8,10],[6,-4]]]) == "No son compatibles"

def test_p_interno():
    assert m.p_interno([[[1,-1]],[[3,0]]],[[[1,1]],[[1,1]]]) == [3,5], "Debe ser 3+5i"

def test_norma():
    assert m.norma([[[4,-9]],[[-2,0]]]) == math.sqrt(101), "Debe ser  (101)^(1/2)"

def test_distancia():
    assert m.distancia([[[1,-1]],[[3,0]]],[[[1,1]],[[1,1]]]) == 3

def test_m_unitaria():
    assert m.m_unitaria([[[5,0],[4,-3]],[[4,3],[-8,0]]]) == "La matriz no es unitaria"

def test_m_hermitiana():
    assert m.m_hermitiana([[[5,0],[4,-3]],[[4,3],[-8,0]]]) == "La matriz es hermitiana"

def test_p_tensorial():
    assert m.p_tensorial([[5,-1],[0,-1]],[[0,0],[4,0]],[[1,1],[2,0]],[[[0,1],[1,0]],[[0,-1],[0,0]]]) == [[[1,5],[5,-1],[1,0],[0,1]],[[-1,5],[0,0],[-1,0],[0,0]],[[0,0],[0,0],[0,4],[4,0]],[[0,0],[0,0],[0,-4],[0,0]],[[-1,1],[1,1],[0,2],[2,0]],[[1,-1],[0,0],[0,-2],[0,0]]]
