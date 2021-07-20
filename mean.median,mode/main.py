import csv

with open('HeightWidth.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

    #sorting
    n = len(new_data)
    new_data.sort()
    print(new_data)

'''n = len(new_data)
total = 0

for x in new_data:
    total+=x

mean = total/n
print("Mean/Average is: " + str(mean))'''