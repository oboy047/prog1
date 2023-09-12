
# Oppretter en liste og fyller den med verdier. En liste kan holde på mange verdier, og vi har lov til å blande datatyper i den.
# Her har vi verdier av datatypen string og int. I tillegg har vi lov til å fylle en liste med andre lister, det har vi også gjort her:
random_list = ["Europe", 7, ["Ny liste", 23, "Med nye elementer"], "Car"]
print(random_list)

# Lager en ny liste med navn på planeter. Listen inneholder 6 elementer (6 planeter):
planeter = ["Merkur", "Venus", "Jorden", "Jupiter", "Saturn", "Uranus"]
print(planeter) # Skriver ut alle elementer i listen

# For å skrive ut ett enkeltelement kan vi gjøre det på følgende måte. Tallet i firkantparentesen er indeksnummer
print(planeter[0])
# NB! Merk at alle lister starter på indeksnummer 0. Altså, det første elementet i lista vil alltid ha indeksnummer 0 ( IKKE 1!)

# Ønsker vi å endre et spesifikt element i listen kan vi gjøre det som under. Under endrer vi elementet med indeksnummer 4 til å være "Mars"
# Dette vil endre det femte elementet i lista (0, 1, 2, 3, 4 <- nr fem når vi starter å telle på 0)
planeter[4] = "Mars"
print(planeter)
