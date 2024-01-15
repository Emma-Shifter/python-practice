import bisect
containersCount = int(input("Количество контейнеров: "))
containers = list(reversed([int(input("Количество контейнеров: ")) for _ in range(containersCount)]))
i = bisect.bisect_left(containers, int(input("Введите вес нового контейнера: ")))
print(f"Номер, который получит новый контейнер: {len(containers) - i + 1}")