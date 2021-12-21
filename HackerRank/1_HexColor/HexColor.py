N = input()

allowedList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e",
               "f"]

for i in range(0, int(N)):
    row = input()
    x = []
    if (row and row[-1] == ';'):
        for j in range(0, int(len(row))):
            x = []
            if row[j] == '#':

                x.append(row[j])

                for p in range(j + 1, len(row)):
                    s = 0
                    for k in range(0, int(len(allowedList))):
                        if row[p] == allowedList[k]:
                            x.append(row[p])
                            s += 1
                            break

                    if s == 0:
                        break

                if len(x) == 4 or len(x) == 7:
                    values = ''.join(x)
                    print(values)
                    continue
                else:
                    x = []


# ---Enter this input---
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }