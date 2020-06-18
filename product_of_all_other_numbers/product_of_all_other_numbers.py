'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    counter = 0
    res = []
    # Loop for each item in list
    while counter < len(arr):
        # if on first item, multiply all items to right, add to answer
        if counter == 0:
            prod = 1
            for i in range(1,len(arr)):
                prod = (prod*arr[i])
            counter += 1
            res.append(prod)
        # if on last item, muultiply all items to left, add to answer
        elif counter == len(arr)-1:
            prod = 1
            for i in range(0,len(arr)-1):
                prod = (prod*arr[i])
            counter += 1
            res.append(prod)
        # if somewhere in middle, add items on left and right
        else:
            left = arr[:counter]
            right = arr[counter+1:]
            prod = 1
            for num in (left + right):
                prod = (prod*num)
            counter += 1
            res.append(prod)
            
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
