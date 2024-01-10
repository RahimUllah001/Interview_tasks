def list_to_reversed(my_list):
    start = 0
    end = len(my_list) - 1

    while start <= end:
        my_list[start] , my_list[end] = my_list[end],my_list[start]
        start += 1
        end -= 1

    return my_list


given_list = [1,2,3,4,5]

r1 = list_to_reversed(given_list)

print(r1)


