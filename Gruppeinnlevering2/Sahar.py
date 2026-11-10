# Interaktiv historie: Erling og medborgerportalen

print("ERLING OG MEDBORGERPORTALEN")
print("----------------------------")

print("Du er Erling og er prosjektleder i kommunen.")
print("Du leder et team som skal lage en digital innbyggerportal.")
print("Teamet ditt har noen konflikter.")
print("Du må ta tre viktige beslutninger.")

# Beslutning 1: Silje og Elias

print()
print("BESLUTNING 1: SILJE OG ELIAS")
print("Silje vil forbedre brukervennligheten.")
print("Elias er bekymret for kostnader og sikkerhet.")

print("Hva skal Erling gjøre?")
print("1. Samle teamet til et felles møte.")
print("2. Snakke med dem hver for seg.")

valg1 = input("Skriv 1 eller 2: ")

while valg1 != "1" and valg1 != "2":
    print("Ugyldig valg. Prøv igjen.")
    valg1 = input("Skriv 1 eller 2: ")

if valg1 == "1":
    print("Erling samler teamet til et møte.")
    print("Begge får forklare sine meninger.")
else:
    print("Erling snakker med dem hver for seg.")
    print("Begge får forklare seg i ro og fred.")

# Beslutning 2: Hamdi og Hallgeir

print()
print("BESLUTNING 2: HAMDI OG HALLGEIR")
print("Hamdi ønsker en kontrollert digital plattform.")
print("Hallgeir ønsker en åpen løsning med innspill fra innbyggerne.")

print("Hva skal Erling gjøre?")
print("1. Samle dem til et felles møte.")
print("2. La dem prøve å løse konflikten selv.")

valg2 = input("Skriv 1 eller 2: ")

while valg2 != "1" and valg2 != "2":
    print("Ugyldig valg. Prøv igjen.")
    valg2 = input("Skriv 1 eller 2: ")

if valg2 == "1":
    print("Erling samler dem til et møte.")
    print("De prøver å finne en løsning sammen.")
else:
    print("Erling lar dem prøve å løse konflikten selv.")
    print("Konflikten kan bli større.")

    # Beslutning 3: Motivasjon i teamet

print()
print("BESLUTNING 3: MOTIVASJON I TEAMET")
print("Flere i teamet begynner å bli frustrerte.")

print("Hva skal Erling gjøre?")
print("1. Arrangere sosiale aktiviteter og teammøter.")
print("2. Bare fokusere på arbeidsoppgavene.")

valg3 = input("Skriv 1 eller 2: ")

while valg3 != "1" and valg3 != "2":
    print("Ugyldig valg. Prøv igjen.")
    valg3 = input("Skriv 1 eller 2: ")

if valg3 == "1":
    print("Erling arrangerer teammøter og sosiale aktiviteter.")
    print("Teamet får bedre muligheter til å samarbeide.")
else:
    print("Erling fokuserer bare på arbeidsoppgavene.")
    print("Noen i teamet kan fortsatt være frustrerte.")

    # Viser valgene som Erling har tatt

print()
print("ERLING HAR TATT ALLE BESLUTNINGENE")
print("Valg 1:", valg1)
print("Valg 2:", valg2)
print("Valg 3:", valg3)

# Bestemmer hvilken slutt historien får

print()
print("SLUTTEN PÅ HISTORIEN")

if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print("SLUTT 1: TEAMET LYKKES!")
    print("Erling legger til rette for godt samarbeid.")
    print("Teamet får bedre tillit og leverer prototypen i tide.")

elif valg1 == "2" and valg2 == "2" and valg3 == "2":
    print("SLUTT 2: PROSJEKTET BLIR FORSINKET.")
    print("Erling griper lite inn i konfliktene.")
    print("Frustrasjonen øker, og samarbeidet blir vanskelig.")
    print("Prosjektet risikerer å bli forsinket.")
else:
    print("SLUTT 3: DELVIS SUKSESS.")
    print("Erling håndterer noen utfordringer, men ikke alle.")
    print("Teamet må fortsette å jobbe med kommunikasjonen.")
    