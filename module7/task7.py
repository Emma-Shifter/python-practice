def getZip(first: iter, second: iter) -> iter:
    for i in range(min(len(first), len(second))):
        yield first[i], second[i]

string = "abcd"
numbers = (10, 20, 30, 40)
print(getZip(string, numbers))
print("\n".join(str(i) for i in getZip(string, numbers)))