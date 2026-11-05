class Componente:
    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        if peso_kg < 0:
            raise ValueError("Il peso del componente non può essere negativo.")

        self.codice = codice
        self.nome = nome
        self.peso_kg = peso_kg