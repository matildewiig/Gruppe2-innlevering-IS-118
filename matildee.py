# Interaktiv historie: Erling og medborgerportalen

def hent_valg(alternativ1, alternativ2):
    """Viser to alternativer og spør til brukeren skriver 1 eller 2."""
    print("  1.", alternativ1)
    print("  2.", alternativ2)
    svar = input("Hva velger Erling? (1 eller 2): ")
    
    # Gjenta spørsmålet helt til svaret er gyldig
    while svar != "1" and svar != "2": 
        print("Ugyldig svar. Skriv bare 1 eller 2.")
        svar = input("Hva velger Erling? (1 eller 2): ")
        
    return svar


# Variabel som teller hvor aktivt Erling har ledet teamet (brukes til slutt)
poeng = 0

# ----------------------------------------------------------------
# INTRODUKSJON
# ----------------------------------------------------------------
print("=== MEDBORGERPORTALEN ===")
print("Du er prosjektleder Erling. Prosjektet har pågått i seks uker,")
print("og teamet er i storming-fasen: Det er mye uenighet.")
print("Første prototype skal være klar om tre uker.")


# ----------------------------------------------------------------
# VALG 1: Konflikten mellom Silje (UX) og Elias (IT)
# ----------------------------------------------------------------
print("\n--- Valg 1: Silje mot Elias ---")
print("UX-designer Silje og IT-rådgiver Elias er uenige om design og teknologi.")
print("Konflikt har blitt personlig. Hva gjør Erling?")

valg1 = hent_valg(
    "Ta konflikten i plenum med hele teamet",
    "Snakke med Silje og Elias hver for seg", 
)

if valg1 == "1": 
    print("\nErling samler teamet. Silje og Elias forklarer hver sin løsning")
    print("og alle får si sin mening. Teamet finner en felles retning.")
    poeng = poeng + 1
else: 
    print("\nErling snakker med Silje og Elias hver for seg. Det blir ro,")
    print("men resten av teamet får ikke vite hva som ble bestemt.")

# -----------------------------------------------------------------
# VALG 2: Konflikten mellom Hamdi (kultur) og Hallgeir (brukerrepresentant)
# -----------------------------------------------------------------
print("\n--- Valg 2: Hamdi mot Hallgeir ---")
print("Hamdi vil ha en kontrollert løsning på kommunens plattform.")
print("Hallgeir vil ha et åpent system med rom for spontane innspill.")
print("Frustrasjonen vokser. Hva gjør Erling?")

valg2 = hent_valg(
    "Møte Hamdi og Hallgeir sammen og lede samtalen",
    "La dem løse det seg i mellom", 
)

if valg2 == "1":
    print("\nErling lytter og holder samtalen nøytral.")
    print("Hamdi og Hallger blir enige om hva innbyggerne skal kunne gjøre i folkemøtene.")
    poeng = poeng + 1
else: 
    print("\nErling holder seg unna. Hamdi og Hallgeir slutter å snakke sammen,")
    print("og frustrasjonen øker uke for uke.")

# ------------------------------------------------------------------
# VALG 3: Motivasjonen i teamet
# ------------------------------------------------------------------
print("\n--- Valg 3: Motivasjon i teamet ---")
print("Fristen nærmer seg, og energien i teamet er lav. Hva gjør Erling?")

valg3 = hent_valg(
    "Satse på trivsel: sosiale aktiviteter og teammøter der alle får si sin mening",
    "Satse kun på fremdrift og fristen"
)

if valg3 == "1":
    print("\nTeamet får bedre samhold og trivsel. Arbeidsmoralen går opp.")
    poeng = poeng + 1
else: 
    print("\nTeamet jobber hardt, men trivselen synker og stemningen blir tung.")

# ---------------------------------------------------------------------
# UTFALL: Avhenger av hvor mange aktive valg (alternativ 1) Erling tok
# ---------------------------------------------------------------------
print("\n=== SLUTTEN ===")

if poeng == 3:
    # Utfall 1: Alle valg var aktive og relasjonsbyggende
    print("UTFALL 1: Teamet lykkes!")
    print("Erling har løst konfliktene gjennom dialog og bygget tillit.")
    print("Teamet går ut av storming-fasen og inn i norming-fasen,")
    print("og prototypen leveres i tide.")
elif poeng >= 1: 
    # Utfall 2: En blanding av aktive og passive valg
    print("UTFALL 2: Teamet leverer en fungerende portal, men løsningen bærer preg av kompromisser.")
    print("Samarbeidsklimaet er fortsatt skjørt.")
else: 
    # Utfall 3: Ingen aktive valg
    print("UTFALL 3: Prosjektet forsinkes.")
    print("Erling har unngått konfliktene, og de har vokst seg større.")
    print("Tilliten er borte, teamet står fast i storming-fasen,")
    print("og prototypen blir ikke ferdig innen fristen.")

# Skriver ut valgene Erling tok (bruker variablene som lagret valgene)
print("\nDine valg: Valg 1 =", valg1, "| Valg 2 =", valg2, "| Valg 3 =", valg3)
print("Takk for at du spilte!")

