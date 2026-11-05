class Componente:
    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        self.codice = codice
        self.nome = nome
        peso = peso_kg
        
        if(peso<=0):
            raise ValueError("il peso non può essere negativo.")