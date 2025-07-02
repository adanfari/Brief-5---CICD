from Backend.modules.calcul import calcul

def test_calcul():
    assert calcul(2) == 4
    assert calcul(-3) == 9
    assert calcul(0) == 0