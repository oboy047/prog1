planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

kjør = True

while kjør:
    print("\n========================================")
    print("== Hva er din vekt på en annen planet? ==")
    print("\n========================================")
    
    for planetnummer in range(len(planeter)):
        print(f"{planetnummer + 1} - {planeter[planetnummer]}")
   
    planetnummer = input("\n Velg en planet ved å skrive et tall")
    planetnummer = int(planetnummer) - 1

    valgt_planet = planeter[planetnummer]
    print(f"\n Du har valgt {valgt_planet}")

    din_vekt = float(input("\n Hva er din vekt på jorda"))

    jordens_tk = tyngdekraft [2]
    din_masse = din_vekt / jordens_tk 
    din_vekt_på_planet = din_masse * tyngdekraft[planetnummer]

    print(f"Din vekt på jorden {valgt_planet} er {round(din_vekt_på_planet , 2)} kg")

    en_gang_til = input("Vil du prøve igjen? Y/N ")

    kjør = en_gang_til.upper() == 'Y'

