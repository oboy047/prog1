brett_spill = ["Ubongo" , "Pandemic", "ticket to ride", "Monopol" , "Mysterium", "Pandemic Legacy : season 0" , 
"Pandemic Legacy : Season 1" ,"Pandemic Legacy : Season 2"]

print(brett_spill[4 : 7])

for spill in brett_spill [-3:]:
    print(spill)

brett_spill.sort()
print(brett_spill)

første_spill = brett_spill[:3]
print(første_spill)

print(brett_spill[::2])

tekst = brett_spill[-3]
print(tekst)
print(f"{tekst[7:15]}")

print(tekst[-1])
print(tekst[-8:])
