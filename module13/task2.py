import os.path

def GeneratePath(path: str = os.path.join(".")) -> list[str]:
    res = []
    for root, dirs, files in os.walk(path):
        res += [os.path.join(root, name) for name in files]
    return res

print(GeneratePath())