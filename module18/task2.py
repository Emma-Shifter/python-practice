import re

carNumbers = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"

privatePattern = re.compile(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}")
taxisPattern = re.compile(r"[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}")

print(f"Список номеров частных автомобилей: {re.findall(privatePattern, carNumbers)}")
print(f"Список номеров такси: {re.findall(taxisPattern, carNumbers)}")