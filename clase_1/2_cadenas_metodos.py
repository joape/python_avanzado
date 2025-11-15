"""
Métodos útiles de cadenas en Python
===================================

🔤 Básicos de formato
------------------------------------
str.upper()       -> Convierte todos los caracteres a mayúsculas.
str.lower()       -> Convierte todos los caracteres a minúsculas.
str.capitalize()  -> Convierte la primera letra a mayúscula y el resto a minúsculas.
str.title()       -> Convierte la primera letra de cada palabra a mayúscula.
str.strip()       -> Elimina espacios (u otros caracteres) al inicio y final.
str.lstrip()      -> Elimina espacios solo al inicio.
str.rstrip()      -> Elimina espacios solo al final.
str.replace(a, b) -> Reemplaza todas las apariciones de 'a' por 'b'.
str.zfill(n)      -> Rellena la cadena con ceros a la izquierda hasta longitud n.

🔍 Búsqueda y comprobación
--------------------------
str.find(sub)     -> Devuelve el índice de la primera aparición de 'sub' o -1 si no se encuentra.
str.rfind(sub)    -> Devuelve el índice de la última aparición de 'sub' o -1 si no se encuentra.
str.index(sub)    -> Igual que find(), pero lanza ValueError si no se encuentra.
str.startswith(prefijo) -> Devuelve True si la cadena comienza con 'prefijo'.
str.endswith(sufijo)    -> Devuelve True si la cadena termina con 'sufijo'.
str.count(sub)    -> Devuelve el número de apariciones de 'sub'.

🧩 División y unión
-------------------
str.split(sep)    -> Divide la cadena en una lista usando 'sep' como separador.
str.rsplit(sep)   -> Divide la cadena desde la derecha.
str.splitlines()  -> Divide la cadena en una lista por saltos de línea.
sep.join(lista)   -> Une los elementos de una lista usando 'sep' como separador.

✅ Validación
------------------------
str.isalpha()     -> True si todos los caracteres son letras.
str.isdigit()     -> True si todos los caracteres son dígitos.
str.isalnum()     -> True si todos los caracteres son alfanuméricos.
str.isspace()     -> True si todos los caracteres son espacios.
str.islower()     -> True si todos los caracteres son minúsculas.
str.isupper()     -> True si todos los caracteres son mayúsculas.
str.istitle()     -> True si la cadena está en formato título.

⚙️ Alineación y formato
--------------------------------
str.center(n, char) -> Centra la cadena en un ancho de n, rellenando con 'char'.
str.ljust(n, char)  -> Alinea a la izquierda en un ancho de n, rellenando con 'char'.
str.rjust(n, char)  -> Alinea a la derecha en un ancho de n, rellenando con 'char'.
"""
