EXTENSIE = '.txt'
KIES_LIJST = 'k'
NIEUWE_LIJST = 'n'
WEERGEEF_LIJST = 'w'
OVERHOREN = 'o'
STOPPEN = 'q'
TOEVOEGEN = 't'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
MAX_WOORDLENGTE = 20
STANDAARD_LIJST = 'NED-EN'

def leeg_scherm():
    for i in range(SCHERMHOOGTE):
        print_regel('')

def main():
    print_header()
    gekozen_lijst = ''
    command = ''
    while command != STOPPEN:
        print_menu(gekozen_lijst)
        command = input(str("| <@> "))
        if command == NIEUWE_LIJST:
            gekozen_lijst = maak_nieuwe_lijst()
        elif command == KIES_LIJST:
            gekozen_lijst = nieuwe_lijst_naam()
        elif command == WEERGEEF_LIJST:
            lijst_weergeven(gekozen_lijst)
        elif command == OVERHOREN:
            overhoren(gekozen_lijst)
        elif command == TOEVOEGEN:
            voeg_woorden_toe(gekozen_lijst)
        leeg_scherm()
    print_afscheid()
        

def nieuwe_lijst_naam():
    print_regel("Kies naam voor de lijst")
    lijst_naam = input(str("| <@> "))
    return lijst_naam

def lijst_weergeven(woordenlijst):
    leeg_scherm()
    f = open(woordenlijst + EXTENSIE)

    for line in f:
        woord1, woord2 = line.strip('\n').split('=')
        print_regel(woord1 + SCHEIDER + woord2)

    f.close()
    print_regel('')
    print_regel("Enter om door te gaan")
    input()

def print_afscheid():
    print_regel("Was gezellig bye bye")
    print_footer()

def print_footer():
    print_regel('')
    print('='*SCHERMBREEDTE)

def print_header():
    print('='*SCHERMBREEDTE)
    print_regel('')

def print_menu(lijst_naam):
    print_regel("Kies " + NIEUWE_LIJST + " om een nieuwe lijst te maken")
    print_regel("Kies " + KIES_LIJST + " om een lijst te kiezen")
    print_regel("Kies " + WEERGEEF_LIJST + " om de woordenlijst te weergeven")
    print_regel("Kies " + OVERHOREN + " om de geselecteerde lijst te overhoren")
    print_regel("Kies " + TOEVOEGEN + " om woorden aan de geselecteerde lijst toe te voegen")
    print_regel("Kies " + STOPPEN + " om te stoppen met het programma")
    print_regel('')
    print_regel("Geselecteerde lijst: " + lijst_naam)

def print_regel(inhoud=''):
    print("| " + inhoud + ' '*(SCHERMBREEDTE-len(inhoud)-4) + " |")

def overhoren(woordenlijst):
    f = open(woordenlijst + EXTENSIE)
    for line in f:
        woord1, woord2 = line.strip('\n').split('=')
        print_regel("Typ " + STOPPEN + " om te stoppen met overhoren")
        print_regel("Wat is de vertaling van: " + woord1)
        gekozen_woord = input(str('| <@> '))
        print_regel('')
        if (gekozen_woord == woord2):
            print_regel("Correct!")
        elif (gekozen_woord == STOPPEN):
            break
        else:
            print_regel("Incorrect!")
        print_regel(woord1 + SCHEIDER + woord2)
        print_regel('')
    f.close()

def voeg_woorden_toe(woordenlijst):
    f = open(woordenlijst + EXTENSIE, 'a')

    while woord != STOPPEN:
        print_regel('Typ het woord dat je wilt toevoegen')
        print_regel('Typ ' + STOPPEN + ' om te stoppen met woorden toe te voegen')
        print_regel('')
        woord = input(str('| <@> '))
        if woord == STOPPEN:
            break
        print_regel('Typ de vertaling van dat woord')
        print_regel('')
        vertaling = input(str('| <@> '))
        f.write(woord + SCHEIDER + vertaling + "\n")
    
    f.close()


def maak_nieuwe_lijst():
    nieuwe_lijst = nieuwe_lijst_naam()
    f = open(nieuwe_lijst + EXTENSIE, "x")

    f.close()
    return nieuwe_lijst

main()
