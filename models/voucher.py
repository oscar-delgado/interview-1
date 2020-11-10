# Oscar Delgado - Interfiew backend for Guell Consulting - 14 Oct 2020
# Time spent: ~5h - Backend design over Python

def Voucher(code, amount, min_amount):
    """
    La función Voucher retorna un diccionario con 
    los nombres de los parámetros y sus valores.
    """
    return {
        'code': code,
        'amount': amount,
        'min_amount': min_amount
    }
    