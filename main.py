from componente import Componente
from robot import Robot


def registra_robot(robot_prodotti: list[Robot], robot: Robot) -> None:

    for registrato in robot_prodotti:
        if registrato.codice.lower() == robot.codice.lower():
            raise ValueError(
                f"Robot con codice {robot.codice} già registrato."
            )

    robot_prodotti.append(robot)


def cerca_robot(
    robot_prodotti: list[Robot],
    codice: str
) -> Robot | None:

    for robot in robot_prodotti:
        if robot.codice.lower() == codice.lower():
            return robot

    return None


def riepilogo_robot(
    nome_azienda: str,
    robot_prodotti: list[Robot]
) -> None:

    print("\n" + "=" * 60)
    print(f"      RIEPILOGO PRODUZIONE - {nome_azienda}")
    print("=" * 60)

    if not robot_prodotti:
        print("Nessun robot registrato.")
        return

    for robot in robot_prodotti:
        print(f"\nCodice: {robot.codice}")
        print(f"Modello: {robot.modello}")
        print(f"Applicazione: {robot.applicazione}")
        print(f"Stato: {robot.stato}")
        print(f"Peso componenti: {robot.peso_componenti():.2f} kg")
        print(f"Numero componenti: {len(robot.componenti)}")

    print("\n" + "=" * 60)


if __name__ == "__main__":

    robot_prodotti: list[Robot] = []

    print("\nCREAZIONE ROBOT E COMPONENTI")


    robot1 = Robot(
        "ROB001", "Atlas X1", "magazzino", 100.0, "in produzione"
    )

    robot2 = Robot(
        "ROB002", "CargoBot 200", "magazzino", 150.0, "in collaudo"
    )

    robot3 = Robot(
        "ROB003", "Assist Pro", "assistenza", 80.0, "pronto"
    )

    robot4 = Robot(
        "ROB004", "LiftMaster", "magazzino", 200.0, "in produzione"
    )



    for robot in [robot1, robot2, robot3, robot4]:
        try:
            registra_robot(robot_prodotti, robot)
            print(f"Robot {robot.codice} registrato correttamente.")

        except ValueError as errore:
            print(f"ERRORE: {errore}")


    # Robot 1
    robot1.aggiungi_componente(
        Componente("C001", "Braccio articolato", 25.0)
    )
    robot1.aggiungi_componente(
        Componente("C002", "Sensore LIDAR", 5.0)
    )

    # Robot 2
    robot2.aggiungi_componente(
        Componente("C003", "Motore elettrico", 40.0)
    )
    robot2.aggiungi_componente(
        Componente("C004", "Telecamera industriale", 3.0)
    )

    # Robot 3
    robot3.aggiungi_componente(
        Componente("C005", "Display touch", 2.0)
    )
    robot3.aggiungi_componente(
        Componente("C006", "Modulo vocale", 1.5)
    )

    # Robot 4
    robot4.aggiungi_componente(
        Componente("C007", "Forche di sollevamento", 60.0)
    )
    robot4.aggiungi_componente(
        Componente("C008", "Sensore di prossimità", 4.0)
    )

    print("\n\n1. RIEPILOGO DELLA PRODUZIONE")

    riepilogo_robot("Physical AI Robotics", robot_prodotti)


    print("\n2. RICERCA ROBOT")

    risultato = cerca_robot(robot_prodotti, "rob001")

    if risultato is not None:
        print(f"Robot trovato: {risultato.codice} - {risultato.modello}")
    else:
        print("Robot non trovato.")

    risultato = cerca_robot(robot_prodotti, "ROB999")

    if risultato is not None:
        print(f"Robot trovato: {risultato.codice}")
    else:
        print("Robot ROB999 non trovato.")


    print("\n3. TEST ROBOT DUPLICATO")

    try:
        robot_duplicato = Robot(
            "ROB001", "Nuovo Atlas", "magazzino", 100.0, "pronto"
        )

        registra_robot(robot_prodotti, robot_duplicato)

    except ValueError as errore:
        print(f"Errore intercettato: {errore}")


    print("\n4. TEST COMPONENTE DUPLICATO")

    try:
        robot1.aggiungi_componente(
            Componente("C001", "Altro braccio articolato", 10.0)
        )

    except ValueError as errore:
        print(f"Errore intercettato: {errore}")



    print("\n5. TEST SUPERAMENTO PESO MASSIMO")

    try:
        robot3.aggiungi_componente(
            Componente("C009", "Struttura metallica", 100.0)
        )

    except ValueError as errore:
        print(f"Errore intercettato: {errore}")


    print("\n6. RICERCA COMPONENTE INESISTENTE")

    componente = robot1.cerca_componente("C999")

    if componente is not None:
        print(f"Componente trovato: {componente.nome}")
    else:
        print("Componente C999 non trovato.")

    print("\n7. RICERCA COMPONENTE ESISTENTE")

    componente = robot1.cerca_componente("C001")

    if componente is not None:
        print(
            f"Componente trovato: {componente.nome} "
            f"({componente.peso_kg} kg)"
        )
    else:
        print("Componente non trovato.")


    print("\n8. RIMOZIONE COMPONENTE")

    componente_rimosso = robot1.rimuovi_componente("C002")

    if componente_rimosso is not None:
        print(
            f"Componente rimosso: {componente_rimosso.nome}"
        )
    else:
        print("Impossibile rimuovere: componente non trovato.")

    print(
        f"Nuovo peso componenti robot1: "
        f"{robot1.peso_componenti():.2f} kg"
    )
    print("\n9. FILTRO COMPONENTI SOTTO PESO")

    peso_massimo = 10.0

    componenti_filtrati = robot1.componenti_sotto_peso(peso_massimo)

    print(f"Componenti con peso <= {peso_massimo} kg:")

    for componente in componenti_filtrati:
        print(
            f"- {componente.nome}: {componente.peso_kg} kg"
        )

    print("\nDIMOSTRAZIONE TERMINATA.")