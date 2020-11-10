# Oscar Delgado - Interfiew backend for Guell Consulting - 14 Oct 2020
# Time spent: ~5h - Backend design over Python

class Cart:
    """
    La clase Cart se inicializa con un atributo 'lista' de elementos vacíos
    y con un atributo 'voucher' con valores iniciales.
    """
    def __init__(self):
        self.list = []
        self.voucher = {
            'code': '',
            'amount': 0,
            'min_amount': 0
        }

    def add_item(self, product, quantity):
        for _ in range(quantity):
            self.list.append(product)

    def get_total(self, country_code):
        total = 0
        for i in range(len(self.list)):
            total += self.list[i].pricing[country_code].finalPrice()
        if total < self.voucher['min_amount']:
            return total
        else: 
            return total - self.voucher['amount']