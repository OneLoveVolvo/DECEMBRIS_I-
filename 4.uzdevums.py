import json

volvo = input("ieraksti json datnes nosaukumu: ")

try:
    with open(volvo, 'r') as opelis:

        mazda = json.load(opelis)

        print(f"vardnicas garums: {len(mazda)}")

        print("vardnicas sledzene:")
        for sledzene in mazda.keys():
            print(sledzene)

        print("vardnicas pievienota vertiba:")
        for vertibapievienota in mazda.values():
            print(vertibapievienota)

        ievadita_sledzene = input("Ievadi sledzeni lai atklatu pievienoto vertibu: ")

        if ievadita_sledzene in mazda:
            print(f"sledzene '{ievadita_sledzene}' pastav un tai pievienota vertiba ir: {mazda[ievadita_sledzene]}")
        else:
            print(f"sledzene '{ievadita_sledzene}' nepastav.")

except FileNotFoundError:
    print(f"date ar nosaukumu '{volvo}' nav atrasta")
except Exception as e:
    print(f"Wrong: {e}")