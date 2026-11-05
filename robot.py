from componente import Componente


class Robot:
    def __init__(
        self,
        codice: str,
        modello: str,
        applicazione: str,
        peso_massimo_componenti_kg: float,
        stato: str
    ) -> None:

        if peso_massimo_componenti_kg < 0:
            raise ValueError("Il peso massimo non può essere negativo.")

        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti: list[Componente] = []

    def aggiungi_componente(self, componente: Componente) -> None:

        if self.cerca_componente(componente.codice) is not None:
            raise ValueError(
                f"Il componente {componente.codice} è già installato."
            )

        nuovo_peso = self.peso_componenti() + componente.peso_kg

        if nuovo_peso > self.peso_massimo_componenti_kg:
            raise ValueError(
                f"Peso massimo superato: {nuovo_peso} kg "
                f"(massimo {self.peso_massimo_componenti_kg} kg)."
            )

        self.componenti.append(componente)

    def peso_componenti(self) -> float:
        return sum(componente.peso_kg for componente in self.componenti)

    def cerca_componente(self, codice: str) -> Componente | None:
        for componente in self.componenti:
            if componente.codice == codice:
                return componente

        return None

    def rimuovi_componente(self, codice: str) -> Componente | None:
        componente = self.cerca_componente(codice)

        if componente is not None:
            self.componenti.remove(componente)
            return componente

        return None

    def componenti_sotto_peso(self, peso_massimo: float) -> list[Componente]:
        return [
            componente
            for componente in self.componenti
            if componente.peso_kg <= peso_massimo
        ]