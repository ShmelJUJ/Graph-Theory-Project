import DinicAlg as da
import networkx as nx
import pytest as pt
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(1500)

def func(test_name):
    f = open("MaxFlow-tests/{0}.txt".format(test_name))
    n, m = f.readline().split(" ")
    n = int(n)
    m = int(m)
    g = da.Graph(n)
    G = nx.DiGraph()
    for i in range(m):
        buf = list(map(int, f.readline().split(" ")))
        g.addEdge(buf[0]-1, buf[1]-1, buf[2])
        G.add_edge(buf[0]-1, buf[1]-1, weight=buf[2])
    start = timer() 
    max_flow_our = g.DinicMaxflow(0, n-1)
    end = timer()
    max_flow_nx = nx.maximum_flow_value(G, 0, n-1, capacity="weight")
    return [max_flow_our, max_flow_nx, end-start, n, m]

def test_1():
    res = func("test_1")
    print("\n test_1:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]    


def test_2():
    res = func("test_2")
    print("test_2:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_3():
    res = func("test_3")
    print("test_3:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_4():
    res = func("test_4")
    print("test_4:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_5():
    res = func("test_5")
    print("test_5:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_6():
    res = func("test_6")
    print("test_6:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_d1():
    res = func("test_d1")
    print("test_d1:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_d2():
    res = func("test_d2")
    print("test_d2:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_d3():
    res = func("test_d3")
    print("test_d3:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_d4():
    res = func("test_d4")
    print("test_d4:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_d5():
    res = func("test_d5")
    print("test_d5:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd01():
    res = func("test_rd01")
    print("test_rd01:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd02():
    res = func("test_rd02")
    print("test_rd02:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd03():
    res = func("test_rd03")
    print("test_rd03:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd04():
    res = func("test_rd04")
    print("test_rd04:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd05():
    res = func("test_rd05")
    print("test_rd05:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd06():
    res = func("test_rd06")
    print("test_rd06:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rd07():
    res = func("test_rd07")
    print("test_rd07:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl01():
    res = func("test_rl01")
    print("test_rl01:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl02():
    res = func("test_rl02")
    print("test_rl02:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl03():
    res = func("test_rl03")
    print("test_rl03:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl04():
    res = func("test_rl04")
    print("test_rl04:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl05():
    res = func("test_rl05")
    print("test_rl05:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl06():
    res = func("test_rl06")
    print("test_rl06:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl07():
    res = func("test_rl07")
    print("test_rl07:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl08():
    res = func("test_rl08")
    print("test_rl08:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl09():
    res = func("test_rl09")
    print("test_rl09:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]

def test_rl10():
    res = func("test_rl10")
    print("test_rl10:    time =", res[2], "s,    N =",res[3], ", M =",res[4])
    assert res[0] == res[1]