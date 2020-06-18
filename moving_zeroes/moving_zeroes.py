'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    non_zero = []
    zero = []
    for num in arr:
        if num != 0:
            non_zero.append(num)
        else:
            zero.append(num)

    return non_zero + zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")