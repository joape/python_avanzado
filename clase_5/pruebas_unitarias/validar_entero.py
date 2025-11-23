from typing import Any


def validar_entero(valor: Any) -> bool:
    if isinstance(valor, bool):
        return False
    if isinstance(valor, str):
        if valor.strip().startswith(("+", "-")):
            # Verifica si el resto de la cadena son dígitos
            # ejemplo: "+123", "-456"
            #           0123    0123
            return valor[1:].isdigit()
        return valor.isdigit()
    return isinstance(valor, int)
