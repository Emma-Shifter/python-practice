def getData(data_count: int, message: str) -> dict:
    data = {}
    for i in range(data_count):
        key = int(input(message.format(i + 1)))
        if (key in data): data[key] += 1
        else: data[key] = 1
    return data


rollers_count = int(input("Количество роликов: "))
rollers = getData(rollers_count, "Размер пары {0}: ")

humans_count = int(input("Количество людей: "))
humans = getData(humans_count, "Размер ноги человека {0}: ")
humans_with_rollers = 0

for human_size in humans.keys():
    if (human_size in rollers):
        humans_with_rollers += min(humans[human_size], rollers[human_size])

print(f"Наибольшее количество людей, которые могут взять ролики: {humans_with_rollers}")