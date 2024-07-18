from math import floor
f = open("17_medium.txt")
data = [int(i) for i in f.readlines()]
mmax, count = 0, 0
f.close()
for i in range(1, len(data) - 2, 2):
    Generation = data[i] \
      + floor(abs(data[i] - data[i - 1]) ** 0.5)
    Delta = abs(data[i + 1] - Generation)
    mmax = max(mmax, Delta)
    if Generation / data[i + 1] >= 0.95:
        count += 1
print(mmax, count)
