array = list(map(int, input().split()))

def get_max_mult(int_array):
    neg1 = float('-inf')  # Largest negative number
    neg2 = float('-inf')  # Second largest negative number
    pos1 = float('inf')   # Smallest positive number
    pos2 = float('inf')   # Second smallest positive number

    for i in int_array:
        if i < 0:
            if i < neg1:  # Find largest negative
                neg2 = neg1
                neg1 = i
            elif i < neg2:  # Find second largest negative
                neg2 = i
        else:
            if i > pos1:
                pos2 = pos1
                pos1 = i
            elif i > pos2:
                pos2 = i

    max_product = float('-inf')
    result_pair = None

    # Check product of two largest negatives
    if neg1 != float('-inf') and neg2 != float('-inf'):
        product_negatives = neg1 * neg2
        if product_negatives > max_product:
            max_product = product_negatives
            result_pair = (neg1, neg2)

    # Check product of two smallest positives
    if pos1 != float('inf') and pos2 != float('inf'):
        product_positives = pos1 * pos2
        if product_positives > max_product:
            max_product = product_positives
            result_pair = (pos1, pos2)

    if result_pair:
        print(min(result_pair), max(result_pair))
    else:
        print("No suitable pairs found")

get_max_mult(array)
