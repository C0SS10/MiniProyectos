import re

def analizar(entrada):
    tokens = []
    i = 0
    while i < len(entrada):
        empareja = None
        # Para emparejar cada expresión regular
        for expReg, tipoToken in [
            (r'[0-9]+(\.[0-9]+)?', 'NUM'),
            (r'[\+\-\*/=%\[\]]', 'OP'),
            (r'\(', 'IPAREN'),
            (r'\)', 'DPAREN'),
        ]:
            patron = re.compile(expReg)
            empareja = patron.match(entrada, i)
            if empareja:
                token = empareja.group(0)
                if tipoToken == 'NUM':
                    tokens.append(("Es un número", token))
                elif tipoToken == 'OP':
                    tokens.append(("Es un operador", token))
                else:
                    tokens.append(("Es un paréntesis", token))
                i = empareja.end(0)
                break
        if not empareja:
            # Si la expresión regular enviada no es valida
            raise ValueError(f"¡ERROR! la entrada que ingresó no es valida {entrada}")
    return tokens