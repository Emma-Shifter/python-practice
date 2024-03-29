import random
PEOPLE_IN_TEAM = 20
def getRandom() -> list:
    return [round(random.uniform(5, 10), 2) for _ in range(PEOPLE_IN_TEAM)]


first_team = getRandom()
second_team = getRandom()
winners = [max(first_team[i], second_team[i])for i in range(PEOPLE_IN_TEAM)]
print(f"Первая команда: {first_team}\nВторая команда: {second_team}\nПобедители тура: {winners}")