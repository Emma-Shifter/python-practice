videoCardsCount = int(input("Количество видеокарт: "))
videoCards = []
max_series = float("-inf")

for i in range(videoCardsCount):
    item = int(input(f"Видеокарта {i + 1}: "))
    videoCards.append(item)
    max_series = max(max_series, item)

print(f"Старый список видеокарт: {videoCards}")
print(f"Новый список видеокарт: {[item for item in videoCards if (item != max_series)]}")