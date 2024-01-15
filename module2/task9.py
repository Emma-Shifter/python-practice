def getId(numbers: list) -> str:
    res = []
    for i in range(len(numbers) - 1, -1, -1):
        if type(numbers[i]) is int and numbers[i] % 2 == 0:
            res.append(str(numbers[i]))
    return "".join(res)

experimentsResults = [1, 2, 3, 4]
print(getId(experimentsResults))