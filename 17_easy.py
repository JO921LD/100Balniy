f = open("17_easy.txt")
data = [int(i) for i in f.readlines()]
f.close()
count, mmin = 0, 99999999
for i in range(len(data) - 5):
    srznach = sum([data[i + j] for j in range(5)]) / 5
    exp = data[i] - data[i + 4] + data[i + 3] + data[i + 2] - data[i + 1]
    if srznach < exp:
        mmin = min(mmin, exp)
        count += 1
print(count, mmin)
