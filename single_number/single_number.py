'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    numbers = []
    for num in arr:
        if num not in numbers:
            numbers.append(num)
        elif num in numbers:
            numbers.remove(num)
            
    return numbers[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")