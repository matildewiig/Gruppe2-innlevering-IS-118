# Oppgave 2

print("Erling er prosjektleder for et team som lager en medborgerportal.")
print("Uenigheten er mellom Silje, Elias og Hamdi og Hallgeir.")
print("Din jobb er å velge hvordan Erling skal håndtere konflikten.")

# Valg nummer 1
print("Scenario 1: Silje og Elias har blitt uenige")
print("Silje har stor fokus på brukervennlighet, men Elias mener hennes prioriteing er urealistisk.")
print("Hva gjør Erling?")
print("1: Samler dem og teamet for å finne en løsning sammen")
print("2: Snakker med dem hver for seg og ber dem prøve å bli enige")

valg1 = input("Velg 1 eller 2: ")

if valg1 == "1":
    print("Silje og Elias forstår hverandre bedre og blir enige om en bedre løsning.")
else:
    print("De blir enige, men ingen av dem er helt fornøyd med løsningen.")

# Valg nummer 2
print("Scenario 2: Hamdi og Hallgeir er uenige.")
print("De er uenige i hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print("Hva gjør Erling?")
print("1: Kaller inn til et felles møte slik at begge kan si sin mening.")
print("2: Lar dem løse det selv imellom hverandre.")

valg2 = input("Velg 1 eller 2: ")

while valg2 != "1" and valg2 != "2":
    print("Du må skrive 1 eller 2")
    valg2 = input("Velg 1 eller 2: ")

if valg2 == "1":
    print("Møtet hjelper, og de to blir enige om hvordan de skal håndtere det og begynner å samarbeide.")
else:
    print("Uenigheten blir værende, og stemningen i teamet blir dårligere.")

# Valg nummer 3
print("Scenario 3: Fristen nærmer seg")
print("Det er lite tid igjen.")
print("Hva gjør Erling?")
print("1: Går gjennom roller, og prater sammen med alle, om hva som skal til for å komme i boks.")
print("2: Presser på for fremdrift og håper det ordner seg")

valg3 = input("Velg 1 eller 2: ")

while valg3 != "1" and valg3 != "2":
    print("Du må skrive 1 eller 2")
    valg3 = input("Velg 1 eller 2: ")

if valg3 == "1":
    print("Alle vet hva de skal gjøre, og teamet jobber mot fristen.")
else:
    print("Teamet blir usikre på hva som er viktigst, og det går saktere.")

# Resultatet av valgene
if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print("UTFALL 1: Teamet blir enige.")
    print("Erling løste konfliktene med å prate sammen, og teamet fikk godt samhold.")
    print("Gruppen kom inn i storming-fasen og leverte prosjektet i tide.")
elif valg2 == "2" and valg3 == "2":
    print("UTFALL 3: Prosjektet forsinkes.")
    print("Konfliktene ble værende, og kommunikasjonen brøt sammen.")
    print("Teamet ble stående fast i storming-fasen og leverte for sent.")
else:
    print("UTFALL 2: Uenigheter blir igjen.")
    print("Teamet leverer portalen, men den bærer fremdeles noen uenigheter mellom Silje og Elias.")
    print("Samarbeidet er halveis, og det kan bli store problemer senere.")
