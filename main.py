def berechne_tarif(alter, mitgliedschaft, ist_premium_erwachsener_sekt=False, ticket_dauer="ganztag"):
    """
    Berechnet den Tarif basierend auf Alter, Mitgliedschaftstyp und weiteren Optionen.
    """
    # Preis-Definitionen
    kinderpreis = 2.5
    jugendermäßigungspreis = 3.5
    erwachsenenpreise = {
        "premium": 3,
        "basis": 4,
        "keine": 5
    }
    tagesticket_preise = {
        "erwachsener": {"ganztag": 10, "premium": 6, "basis": 8},
        "kind": {"ganztag": 5},
        "jugendlich": {"ganztag": 6}
    }

    # Preisberechnung basierend auf Alter und Mitgliedschaft
    if alter < 14:
        preis = kinderpreis
    elif 14 <= alter <= 17:
        preis = jugendermäßigungspreis
    else:
        # Erwachsenentarif basierend auf Mitgliedschaft
        preis = erwachsenenpreise.get(mitgliedschaft, 5)
        # Aufschlag für Sektoption für Premium-Mitglieder
        if mitgliedschaft == "premium" and ist_premium_erwachsener_sekt:
            preis += 0.75

    # Anpassung für Ticketdauer-Optionen
    if ticket_dauer == "halbtags":
        if alter < 14:
            preis = tagesticket_preise["kind"]["ganztag"] / 2
        elif 14 <= alter <= 17:
            preis = tagesticket_preise["jugendlich"]["ganztag"] / 2
        else:
            preis = tagesticket_preise["erwachsener"].get(mitgliedschaft,
                                                          tagesticket_preise["erwachsener"]["ganztag"]) / 2
    else:
        # Ganztagesticket-Preise
        if alter < 14:
            preis = tagesticket_preise["kind"]["ganztag"]
        elif 14 <= alter <= 17:
            preis = tagesticket_preise["jugendlich"]["ganztag"]
        else:
            preis = tagesticket_preise["erwachsener"].get(mitgliedschaft, tagesticket_preise["erwachsener"]["ganztag"])

    return preis


def main():
    while True:
        # Eingabe des Alters vom Nutzer
        try:
            alter = int(input("Bitte geben Sie das Alter ein: "))
            if alter < 0:
                print("Ungültiges Alter. Bitte versuchen Sie es erneut.")
                continue
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie ein gültiges Alter ein.")
            continue

        # Mitgliedschaftsart für Erwachsene abfragen
        if alter >= 18:
            mitgliedschaft = input("Geben Sie die Mitgliedschaft an (premium/basis/keine): ").strip().lower()
            ist_premium_erwachsener_sekt = (mitgliedschaft == "premium" and input(
                "Möchten Sie ein Glas Sekt für 0,75 € hinzufügen? (ja/nein): ").strip().lower() == "ja")
        else:
            mitgliedschaft = "keine"  # Keine Mitgliedschaft für Kinder/Jugendliche
            ist_premium_erwachsener_sekt = False

        # Ticketdauer auswählen
        ticket_dauer = input("Wählen Sie die Ticketdauer (halbtags/ganztag): ").strip().lower()
        if ticket_dauer not in ["halbtags", "ganztag"]:
            print("Ungültige Option. Es wird standardmäßig ein Ganztagesticket ausgewählt.")
            ticket_dauer = "ganztag"

        # Tarif berechnen
        preis = berechne_tarif(alter, mitgliedschaft, ist_premium_erwachsener_sekt, ticket_dauer)
        print(f"Der berechnete Tarif beträgt: €{preis:.2f}")

        # Abfrage, ob der Nutzer einen weiteren Tarif berechnen möchte
        weiter = input("Möchten Sie einen weiteren Tarif abfragen? (ja/nein): ").strip().lower()
        if weiter != "ja":
            break

    print("Vielen Dank! Wir wünschen Ihnen einen angenehmen Besuch.")


if __name__ == "__main__":
    main()
