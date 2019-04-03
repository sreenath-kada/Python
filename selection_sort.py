def selection_sort(list):

    for i in range(len(list)):
        min_index = i

        for j in range(i, len(list)):
           if list[min_index] > list[j]:
               min_index = j

        list[i], list[min_index] = list[min_index], list[i]


list = [19,2,31,45,30,11,121,27]
selection_sort(list)
print(list)
