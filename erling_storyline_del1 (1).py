# Gruppeoppgave 2 - IS-118
# Interaktiv historie basert pa gruppens storyline i del 1

print('Velkommen til prosjektet om kommunens digitale medborgerportal!')
print('Du spiller som Erling, som er prosjektleder.')
print('Etter seks uker har det oppstatt konflikter i gruppen.')
print('Den forste prototypen skal vaere ferdig om tre uker.')
print('Du skal ta tre valg som bestemmer hvordan prosjektet ender.')

# Holder styr pa valg som bidrar til felles samarbeid og dialog.
poeng = 0

# Beslutning 1: Silje og Elias
print('\nBeslutning 1: Silje og Elias')
print('Silje og Elias er uenige om design, sikkerhet og kostnader.')
print('Uenigheten har blitt personlig. Hva vil du gjore?')
print('1. Ta konflikten opp i plenum med hele teamet.')
print('2. Snakke med Silje og Elias hver for seg.')
valg1 = input('Velg 1 eller 2: ')
while valg1 != '1' and valg1 != '2':
    print('Ugyldig valg. Prov igjen.')
    valg1 = input('Velg 1 eller 2: ')

if valg1 == '1':
    print('Hele teamet far hore begge sider av saken.')
    print('Flere forstar problemet, men motet blir litt opphetet.')
    print('Erling hjelper gruppen med a finne en felles retning.')
    poeng = poeng + 1
elif valg1 == '2':
    print('Silje og Elias far snakke fritt i hver sin samtale.')
    print('Konflikten roer seg, men resten av teamet far ikke felles avklaring.')

# Tidligere valg pavirker hvordan neste situasjon oppleves.
print('\nDet oppstar na uenighet mellom Hamdi og Hallgeir.')
if valg1 == '1':
    print('Etter fellesmotet er flere mer villige til a diskutere uenigheter apent.')
else:
    print('Siden teamet ikke fikk en felles avklaring, er samarbeidet fortsatt sarbart.')

# Beslutning 2: Hamdi og Hallgeir
print('\nBeslutning 2: Hamdi og Hallgeir')
print('Hamdi vil bruke kommunens kontrollerte plattform.')
print('Hallgeir vil ha mer apne digitale folkemoter.')
print('Hva vil du gjore?')
print('1. Samle Hamdi og Hallgeir til et mote og lytte til begge.')
print('2. La Hamdi og Hallgeir lose problemet selv.')
valg2 = input('Velg 1 eller 2: ')
while valg2 != '1' and valg2 != '2':
    print('Ugyldig valg. Prov igjen.')
    valg2 = input('Velg 1 eller 2: ')

if valg2 == '1':
    print('De far forklare synspunktene sine og finner et mulig kompromiss.')
    print('Det blir lettere a samarbeide videre.')
    poeng = poeng + 1
elif valg2 == '2':
    print('Erling blander seg ikke inn.')
    print('Hamdi og Hallgeir blir ikke enige, og frustrasjonen vokser.')

# Beslutning 3: motivasjon og fremdrift
print('\nBeslutning 3: Motivasjon i teamet')
if poeng == 2:
    print('Stemningen er bedre, men teamet er slitent for fristen.')
elif poeng == 1:
    print('Noe er lost, men flere er fortsatt frustrerte.')
else:
    print('Stemningen er spent, og samarbeidet er vanskelig.')
print('Prototypen skal leveres om tre uker. Hva vil du gjore?')
print('1. Prioritere relasjonsbygging, trivsel og et felles teammote.')
print('2. Prioritere fremdrift og be alle konsentrere seg om oppgavene.')
valg3 = input('Velg 1 eller 2: ')
while valg3 != '1' and valg3 != '2':
    print('Ugyldig valg. Prov igjen.')
    valg3 = input('Velg 1 eller 2: ')

if valg3 == '1':
    print('Teamet far snakket sammen og bygger mer tillit.')
    print('De finner tilbake til motivasjonen.')
    poeng = poeng + 1
elif valg3 == '2':
    print('Teamet jobber videre, men flere er fortsatt misfornoyde.')
    print('Presset kan gjore samarbeidet vanskeligere.')

# Tre mulige sluttresultater fra storylinen i del 1
print('\nProsjektets resultat:')
if poeng == 3:
    print('Utfall 1: Teamet lykkes og nar norming fasen.')
    print('Tilliten blir sterkere, og prototypen leveres i tide.')
elif poeng == 1 or poeng == 2:
    print('Utfall 2: Delvis maloppnaelse og sarbart samarbeid.')
    print('Prosjektet gar videre, men flere konflikter er ikke helt lost.')
else:
    print('Utfall 3: Prosjektet blir forsinket.')
    print('Konfliktene vokser, og prototypen blir ikke ferdig i tide.')

print('\nTakk for at du spilte!')
