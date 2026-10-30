# Konflikthåndtering

print("Du er prosjektleder for den nye medborgerportalen.")
print("Du må ta noen viktige valg som vil påvirke prosjektet.")


# Valg 1

print("Silje og Elias er uenige.")
print("Silje vil ha en brukervennlig portal, Elias mener Siljes forslag er urealistisk, usikkert og for kostbart.")
print("Hva gjør du?")
print("1. Samler dem til et møte for å finne en løsning.")
print("2. Snakker med dem hver for seg.")

valg1 = input("Velg 1 eller 2: ")

if valg1 == "1":
    print("Silje og Elias snakker sammen og finner en løsning.")
else:
    print("De finner et kompromiss, men er fortsatt litt uenige.")


# Valg 2

print("Hamdi og Hallgeir har også en konflikt.")
print("Hva gjør du?")
print("1. Samler dem til et møte for å løse problemet.")
print("2. Lar dem prøve å løse problemet selv.")

valg2 = input("Velg 1 eller 2: ")

if valg2 == "1":
    print("De får snakket sammen og forstår hverandre bedre.")
else:
    print("Konflikten fortsetter, og samarbeidet blir dårligere.")


# Valg 3

print("Prosjektet nærmer seg fristen.")
print("Hva gjør du?")
print("1. Følger opp teamet og passer på at alle samarbeider.")
print("2. Fokuserer bare på oppgavene og lar konfliktene være.")

valg3 = input("Velg 1 eller 2: ")

if valg3 == "1":
    print("Teamet får bedre oversikt og samarbeider bedre.")
else:
    print("Motivasjonen blir lavere og prosjektet går tregere.")


# Resultat

print("Slik gikk det med prosjektet:")

if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print("UTFALL 1:Prosjektet blir en suksess.")
    print("Alle samarbeider bedre og stoler mer på hverandre.")
    print("Teamet blir ferdig og leverer medborgerportalen i tide.")

elif valg1 == "2" and valg2 == "2" and valg3 == "2":
    print("UTFALL 3: Prosjektet blir forsinket.")
    print("Konfliktene blir ikke løst, og samarbeidet blir dårligere.")
    print("Teamet mister motivasjonen, og medborgerportalen blir forsinket.")

else:
    print("UTFALL 2: Prosjektet blir en delvis suksess.")
    print("Teamet klarer å lage en fungerende medborgerportal.")
    print("Men noen konflikter er fortsatt ikke løst, og samarbeidet er vanskelig.")


