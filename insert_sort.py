def insert_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        nextElem = list[i]

        while list[j] > nextElem and j >= 0:
            list[j+1] = list[j]
            j = j - 1

        list[j+1] = nextElem


list = [19,2,31,45,30,11,121,27]

insert_sort(list)
print(list)

