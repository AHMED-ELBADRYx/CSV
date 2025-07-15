# CSV explanation

import csv

counts = {} # Or counts = dict()
with open(r"CSV Projects\Explanation\file.csv", "r") as myfile:
    reader = csv.DictReader(myfile)
    # DictReader calls its values ​​as keys, while reader method only depends on the index. We use next(reader) in the line after it to leave the first row of attributes.
    for row in reader:
        name = row["name"].strip().upper() # Or row[0] if reader
        if name not in counts:
            counts[name] = 0
        counts[name] +=1

# sorted: arranges data alphabetically
# reverse: reverse the order
# key =: Sorts based on values (scores), not keys.
for c in sorted(counts, key = lambda name: counts[name], reverse=True):
    print(f"{c}: {counts[c]}")

# ………………………………………

import csv

get_data = input("name: ").upper().strip()
counts = 0
with open(r"CSV Projects\Explanation\file.csv", "r") as myfile:
    reader = csv.DictReader(myfile)
    for row in reader:
        name = row["name"].upper().strip()
        if get_data == name:
            counts += 1
    print(counts)