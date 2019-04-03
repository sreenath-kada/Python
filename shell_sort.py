def shell_sort(list):

    gap = len(list) // 2

    while gap > 0 :

        for i in range(gap, len(list)):
            nextElem = list[i]
            j = i

            while j >= gap and list[j - gap] > nextElem:
                list[j] = list[j - gap]
                j = j - gap
            list[j] = nextElem

        gap = gap // 2

list = [19,2,31,45,30,11,121,27]

shell_sort(list)
print(list)
