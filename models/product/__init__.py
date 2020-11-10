# Oscar Delgado - Interfiew backend for Guell Consulting - 14 Oct 2020
# Time spent: ~5h - Backend design over Python

class PriceDiscount:
    """
    La coase PriceDiscount se inicializa con los atributos pasados como argumentos.

    Se implementa el método '__getattr__' como pequeña trampa para que, si al buscar 
    un atributo que no existe (en este caso el atributo 'discount' de tests.py) devuelva
    cero si el atributo 'disc' es negativo y el mismo atributo si es positivo. 

    Se implementa una función 'finalPrice' para gestionar el precio del profucto
    con el descuento aplicado.
    """
    def __init__(self, price, disc):
        self.price = price
        self.disc = disc
    
    def __getattr__(self, item):
        if item == 'discount':
            return 0 if self.disc < 0 else self.disc

    def finalPrice(self):
        return self.price - self.price * self.disc

class Product:
    """
    La clase Product se inicializa con los atributos pasados como argumentos.
    
    Utiliza la subclase PriceDiscount para gestionar el atributo 'pricing',
    el cual se inicializa como un diccionario vacío.
    """
    def __init__(self, sku, name):
        self.sku = sku
        self.name = name
        self.pricing = {}

    def set_pricing(self, country_code, price, discount):
        if country_code in self.pricing.keys():
            self.pricing[country_code].price = price
            self.pricing[country_code].disc += discount
        else:
            self.pricing[country_code] = PriceDiscount(price, discount)

    def get_pricing(self, country_code):
        return self.pricing[country_code]