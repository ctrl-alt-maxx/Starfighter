import csv

# list = [110, 52, 4, 500, 20]

# sorting the list in ascending order
# list.sort(reverse=True)

# print(list)

# list.sort()

# print(list)

# ACCÈS AU FICHIER
with open("StarFighter.csv", "r", newline="\n") as scorefile:
    reader = csv.reader(scorefile)
    data = list(reader)
    
scoreslist = []
for i, row in enumerate(data):
    scoreslist.append(row[0])    
    
def get_pts(score):
    return score.get('Points')    
    
scoreslist.sort(key=lambda x: x.get('Points'))
print(scoreslist)