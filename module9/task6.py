from collections import Counter
from zipfile import ZipFile

with ZipFile("voina-i-mir.zip") as vimZip:
    with vimZip.open("voina-i-mir.txt") as file:
        cleanString = "".join([chr(char) for i in file.readlines() for char in i.rstrip()])

data = dict(Counter(cleanString))

print(data)