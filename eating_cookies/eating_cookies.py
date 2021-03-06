'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # when cookies = 0 - base case
    # when cookies < 0 - base case
    # when cookies >= 1 - eating cookies

    if n == 0:
        return 1
    if n < 0:
        return 0
    if n >= 1:
        return eating_cookies(n-3)+eating_cookies(n-2)+eating_cookies(n-1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
