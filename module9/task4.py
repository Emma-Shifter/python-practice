passed = []
with open("first_tour.txt", "r", encoding="UTF-8") as firstFile:
    pointsNeed = int(firstFile.readline())
    for line in firstFile.readlines():
        surname, name, points = line.rstrip().split()
        points = int(points)
        if (points > pointsNeed): passed.append((points, surname, name))

passed = tuple(reversed(sorted(passed)))
with open("second_tour.txt", "w", encoding="UTF-8") as secondFile:
    line_break = "\n"
    secondFile.write(
        f"{len(passed)}{line_break}"
        f"{line_break.join([f'{i + 1}) {passed[i][2][0]}. {passed[i][1]} {passed[i][0]}' for i in range(len(passed))])}"
    )