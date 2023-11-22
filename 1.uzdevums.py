volvo= input("ievadi datnes nosaukumu: ")

try:
    with open(volvo, 'r') as datne:
        volvo_saturs = datne.read()


        print(f"simbolu skaits datne: {len(volvo_saturs)}")

        print(f"pirmie 10 simboli: {volvo_saturs[:10]}")

        print(f"pirmais simbols: {volvo_saturs[0]}, pedejais simbols: {volvo_saturs[-1]}")

        garums = int(input("ievadi garumu: "))

        if garums == len(volvo_saturs):
            print("ierakstitais garums sakrit")
            print(f"simboli no sākuma lidz {garums}: {volvo_saturs[:garums]}")
        else:
            print("ierakstitais garums neatbilst datnei")
except FileNotFoundError:
    print(f"datne ar nosaukumu '{volvo}' nav atrasta")
except Exception as e:
    print(f"wong: {e}")