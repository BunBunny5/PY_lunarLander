altitude = 1500
carburant_hydrogene = 2000
HYPERVITESSE = 60 #vélocité
EXPLOSIOOOOON = 0 #temps avant impact
attraction = 1.622 #gravité
REACTIOOON = 0 #force du propulseur

while altitude > 0:
    EXPLOSIOOOOON = altitude/HYPERVITESSE
    print("EXPLOSIOOOOON DANS..." , EXPLOSIOOOOON)
    print("HYPERVITESSE = " , HYPERVITESSE)
    print("hydrogene restant = " , carburant_hydrogene)
    print("Niveau altitude" , altitude)
    inputGood = False
    while inputGood == False:
        try:
            REACTIOOON = float(input("Hi burn some hydrogene for a nice landing, an amount between 0 and 60!"))
            inputGood = True
        except ValueError:
            print ("Number please")
    if carburant_hydrogene <= 0:
        REACTIOOON = 0
        carburant_hydrogene = 0
    HYPERVITESSE += attraction - REACTIOOON / 10
    altitude -= HYPERVITESSE
    carburant_hydrogene -= REACTIOOON
    print()
if HYPERVITESSE >= 5:
        print ("BOOM!")
        print ("GAME-OVER!")

else:
        print("mission Successed!")
