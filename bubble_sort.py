def bubble_sort(list):
    for passNum in range(len(list) - 1, 0 , -1):
        for idx in range(passNum):
            if list[idx] > list[idx+1]:
                tmp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = tmp


list = [23, 45, 12, 2, 5, 8, 9, 10, 15, 19, 31, 40]
bubble_sort(list)
print(list)

