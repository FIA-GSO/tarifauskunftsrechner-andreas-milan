# Sprachpaket für mehrsprachige Unterstützung
languages = {
    "en": {
        "invalid_language": "Not a valid Language!",
        "invalid_age": "Invalid age. Please try again.",
        "invalid_input": "Invalid input. Please enter a valid age.",
        "enter_age": "Please enter your age: ",
        "membership_prompt": "Enter membership type (premium/basic/none): ",
        "add_sekt": "Would you like to add a glass of sekt for €0.75? (yes/no): ",
        "ticket_duration": "Choose ticket duration (half-day/full-day): ",
        "invalid_option": "Invalid option. A full-day ticket is selected by default.",
        "calculated_rate": "The calculated rate is: €",
        "another_rate": "Would you like to calculate another rate? (yes/no): ",
        "thank_you": "Thank you! We wish you a pleasant visit."
    },
    "de": {
        "invalid_language": "Keine gültige Sprache!",
        "invalid_age": "Ungültiges Alter. Bitte versuchen Sie es erneut.",
        "invalid_input": "Ungültige Eingabe. Bitte geben Sie ein gültiges Alter ein.",
        "enter_age": "Bitte geben Sie das Alter ein: ",
        "membership_prompt": "Geben Sie die Mitgliedschaft an (premium/basis/keine): ",
        "add_sekt": "Möchten Sie ein Glas Sekt für 0,75 € hinzufügen? (ja/nein): ",
        "ticket_duration": "Wählen Sie die Ticketdauer (halbtags/ganztag): ",
        "invalid_option": "Ungültige Option. Es wird standardmäßig ein Ganztagesticket ausgewählt.",
        "calculated_rate": "Der berechnete Tarif beträgt: €",
        "another_rate": "Möchten Sie einen weiteren Tarif abfragen? (ja/nein): ",
        "thank_you": "Vielen Dank! Wir wünschen Ihnen einen angenehmen Besuch."
    }
}


def calculate_rate(age, membership, is_premium_with_sekt=False, ticket_duration="full-day"):
    # Preisdefinitionen
    child_price = 2.5
    youth_discount_price = 3.5
    adult_prices = {
        "premium": 3,
        "basic": 4,
        "none": 5
    }
    day_ticket_prices = {
        "child": {"full-day": 5},
        "youth": {"full-day": 6},
        "adult": {"full-day": 10, "premium": 6, "basic": 8}
    }

    # Preisberechnung basierend auf dem Alter und der Mitgliedschaft
    if age < 14:
        price = child_price
    elif 14 <= age <= 17:
        price = youth_discount_price
    else:
        price = adult_prices.get(membership, 5)
        # Aufschlag für Sektoption für Premium-Mitglieder
        if membership == "premium" and is_premium_with_sekt:
            price += 0.75

    # Anpassung des Preises je nach Ticketdauer
    if ticket_duration == "half-day":
        if age < 14:
            price = day_ticket_prices["child"]["full-day"] / 2
        elif 14 <= age <= 17:
            price = day_ticket_prices["youth"]["full-day"] / 2
        else:
            price = day_ticket_prices["adult"].get(membership, day_ticket_prices["adult"]["full-day"]) / 2
    else:
        if age < 14:
            price = day_ticket_prices["child"]["full-day"]
        elif 14 <= age <= 17:
            price = day_ticket_prices["youth"]["full-day"]
        else:
            price = day_ticket_prices["adult"].get(membership, day_ticket_prices["adult"]["full-day"])

    return price


def main():
    while True:
        # Sprachwahl
        try:
            language = input("en/de? ").strip().lower()
            if language not in languages:
                print("Not a valid Language!")
                continue
        except ValueError:
            print("Not a valid Language, please enter (en/de)")
            continue

        # Laden der Übersetzungstexte für die gewählte Sprache
        text = languages[language]

        # Eingabe des Alters
        try:
            age = int(input(text["enter_age"]))
            if age < 0:
                print(text["invalid_age"])
                continue
        except ValueError:
            print(text["invalid_input"])
            continue

        # Abfrage der Mitgliedschaft und Sektoption für Erwachsene
        if age >= 18:
            membership = input(text["membership_prompt"]).strip().lower()
            is_premium_with_sekt = (membership == "premium" and
                                    input(text["add_sekt"]).strip().lower() == ("ja" if language == "de" else "yes"))
        else:
            membership = "none"
            is_premium_with_sekt = False

        # Abfrage der Ticketdauer
        ticket_duration = input(text["ticket_duration"]).strip().lower()
        if ticket_duration not in ["half-day", "full-day", "halbtags", "ganztag"]:
            print(text["invalid_option"])
            ticket_duration = "ganztag" if language == "de" else "full-day"

        # Berechnung des Preises
        price = calculate_rate(age, membership, is_premium_with_sekt, ticket_duration)
        print(f"{text['calculated_rate']}€{price:.2f}")

        # Abfrage, ob der Nutzer einen weiteren Tarif berechnen möchte
        more = input(text["another_rate"]).strip().lower()
        if more != ("ja" if language == "de" else "yes"):
            break

    print(text["thank_you"])


if __name__ == "__main__":
    main()
