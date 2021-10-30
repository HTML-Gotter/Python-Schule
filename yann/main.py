# Shift + F10 = Programm Start
# Strg + F2 = Programm Stoppen
# Strg + K = Commit
# Strg + T = Update

def answer_check(answer): # Definieren einer Funktion
    if "!" in answer.lower(): # Wenn - Dann
        print("Ihre Antwort wird verarbeitet")
    else:
        print("Ihre Antwort wurde abgelehnt")
    return answer.lower() # Wert zurückgeben


antwort = answer_check( # Funktion answer_check() aufrufen und Wert erhalten
    input("Wie ist ihr Name? ") # Nutzer nach Namen fragen
)


print(antwort) # Wert der Funktion ausgeben

