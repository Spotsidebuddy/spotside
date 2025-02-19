import sys

array = list(map(int, input().split()))


def get_max_mult(int_array):
    if len(int_array) >= 3:
        max1 = max(int_array[:3])
        max2 = max(*int_array[:3].remove(max1))
        max3 = max(*int_array[:3].remove(max2).remove(max1))
        min1 = min(int_array[:3])
        min2 = min(*int_array[:3].remove(min1))

        for i in range(2, len(int_array)):
            #for maximums 3 switches
            if int_array[i] > max1:
                max3 = max2
                max2 = max1
                max1 = int_array[i]
            elif int_array[i] > max2:
                max3 = max2
                max2 = int_array[i]
            elif int_array[i] > max3:
                max3 = int_array[i]
            #for nagatives same from last
            elif int_array[i] < min1:
                min2 = min1
                min1 = int_array[i]
            elif int_array[i] < min2:
                min2 = int_array[i]

        max_mult = max1 * max2 * max3
        min_mult = min1 * min2 * max1

        if max_mult >= min_mult:
            print(max1, max2, max3)
        else:
            print(min1, min2, max1)








get_max_mult(array)
