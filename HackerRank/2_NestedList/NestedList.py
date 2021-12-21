for _ in range(int(input())):
    name = input()
    score = float(input())
    studentDict[name] = score

sortedStudentList = sorted(set(studentDict.values()))
secondHighest = sortedStudentList[1]

result = []
for k, v in studentDict.items():
    if (studentDict[k] == secondHighest):
        result.append(k)

print(*sorted(result), sep="\n")
