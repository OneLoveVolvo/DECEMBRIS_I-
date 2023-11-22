import datetime

tgd_stunda = datetime.datetime.now().hour

if 6 <= tgd_stunda < 12:
    print("Labsriits")
elif 12 <= tgd_stunda < 18:
    print("Labadiena")
else:
    print("Labsvakars kaimin maja")