altitude = 1500
carburant_hydrogene = 2000
HYPERVITESSE = 60
EXPLOSIOOOOON = 40
attraction = 1.622
REACTIOOON = 0

while altitude > 0:
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
    
if HYPERVITESSE >= 5:
        print ("BOOM!")
        print ("GAME-OVER!")

else:
        print("mission Successed!")
