import csv

volvo = input("ievadi csv datnes nosaukumu: ")

try:
    with open(volvo, 'r') as csv_datne:

        volvo_masivs = list(csv.reader(csv_datne))

        print(f"Masiīva garums: {len(volvo_masivs)}")

        if len(volvo_masivs) > 0:
            print(f"Pirmais elements: {volvo_masivs[0]}")

        print("Pirmie 5 elementi:")
        for elements in volvo_masivs[:5]:
            print(elements)

except FileNotFoundError:
    print(f"Datne ar nosaukumu '{volvo}' nav atrasta.")
except Exception as e:
    print(f"Kļūda: {e}")