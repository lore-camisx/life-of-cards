class Carta:
    VALORES = ['A', '2', '3', '4', '5', '6', '7']
    NAIPES = ['Paus', 'Copas', 'Espadas', 'Ouros']

    FORCA_VALOR = {
        'A': 7,
        '2': 6,
        '3': 5,
        '4': 4,
        '5': 3,
        '6': 2,
        '7': 1,
    }

    FORCA_NAIPE = {
        'Paus': 4,
        'Copas': 3,
        'Espadas': 2,
        'Ouros': 1,
    }

    def __init__(self, valor, naipe):
        if valor not in self.VALORES:
            raise ValueError(f"Valor inválido: {valor}")
        if naipe not in self.NAIPES:
            raise ValueError(f"Naipe inválido: {naipe}")
        self.valor = valor
        self.naipe = naipe

    def forca(self):
        return self.FORCA_VALOR[self.valor]

    def forca_naipe(self):
        return self.FORCA_NAIPE[self.naipe]

    def forca_total(self):
        return (self.forca() * 10) + self.forca_naipe()

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

    def __repr__(self):
        return f"Carta('{self.valor}', '{self.naipe}')"

    def __eq__(self, other):
        return isinstance(other, Carta) and self.valor == other.valor and self.naipe == other.naipe

    def __hash__(self):
        return hash((self.valor, self.naipe))