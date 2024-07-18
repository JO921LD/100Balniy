f = open("17_hard.txt")
data = [list(map(int, i.split())) for i in f.readlines()]
f.close()
# Максимальный использованный объём, объём за год
mmax, total_year_use = 0, 0
# замен, актуальный год, максимальный год
changed, year, res_year = 0, 1, 0
temp = [100, 100, 100, 100]
for i in data[1:]:
    for j in range(4):
        if i[j + 1] == 100:
            changed += 1
            total_year_use += temp[j]
        else:  
            total_year_use += temp[j] - i[j + 1]
        temp[j] = i[j + 1]
    if i[0] != year:
        if total_year_use > mmax:
            mmax = total_year_use
            res_year = year
        total_year_use = 0
        year = i[0]
print(changed, res_year)
