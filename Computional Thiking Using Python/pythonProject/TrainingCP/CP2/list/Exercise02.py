list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
list2 = [1, 3, 5, 7, 8, 9, 11, 13, 15, 17]
listAll = []

for i in range(10):
    listAll.append(list2[i])
    listAll.append(list1[i])

print(f"Lista com todos os números: {listAll}")
