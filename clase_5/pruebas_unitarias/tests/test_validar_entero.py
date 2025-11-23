from validar_entero import validar_entero


def test_validar_entero_con_entero_positivo():
    assert validar_entero(5) is True


def test_validar_entero_con_entero_negativo():
    assert validar_entero(-3) is True


def test_validar_entero_con_cero():
    assert validar_entero(0) is True


def test_validar_entero_con_flotante():
    assert validar_entero(4.5) is False


def test_validar_entero_con_cadena_no_válida():
    assert validar_entero("texto") is False


def test_validar_entero_con_cadenas_válidas():
    assert validar_entero("+1") is True
    assert validar_entero("-1") is True


def test_validar_entero_con_lista():
    assert validar_entero([1, 2, 3]) is False


def test_validar_entero_con_diccionario():
    assert validar_entero({"clave": "valor"}) is False


def test_validar_entero_con_none():
    assert validar_entero(None) is False


def test_validar_entero_con_booleano():
    assert validar_entero(True) is False
