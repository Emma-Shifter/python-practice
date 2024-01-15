import json

with open("old.json", "r", encoding="UTF-8") as json_old_file:
    oldJson = dict(json.load(json_old_file))
with open("new.json", "r", encoding="UTF-8") as json_new_file:
    newJson = dict(json.load(json_new_file))

diffList = {"services", "staff", "datetime"}

def get_a(old: dict, new: dict, diffs: dict):
    for key in old.keys():
        if key in old and key in new:
            if (type(old[key]) is dict and type(new[key]) is dict): get_a(old[key], new[key], diffs)
            else:
                if (key in diffList and old[key] != new[key]):diffs[key] = new[key]

diffs = {}
get_a(oldJson, newJson, diffs)
print(diffs)

with open("result.json", "w", encoding="UTF-8") as file:
    json.dump(diffs, file, ensure_ascii=False, indent=4)