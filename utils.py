#utils.py (opcional): funções auxiliares, como validação de entrada.

def validar_numero(entrada: str) -> bool:
    """Valida se a entrada é um número."""
    try:
        float(entrada)
        return True
    except ValueError:
        return False
    
