
num_points = 5
key_list = []
for i in range(num_points):
    x = i + 1
    key_list.append("Point" + str(x))
print(key_list)

list_x = [1,2,3,4,5,6,7]

for i in range(5):
    for x in range(7):
        key_list[i].append(list_x[x])

print(key_list)