'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

'''
PLAN
    # Loop through the array
    # Mark the first number to compare to other numbers
    # If the same one comes around then remove those numbers
    # Remove all the numbers until the odd one out is left.
'''
def single_number(arr):
    # Your code here
    current = arr[0]
    for number in arr[1:]:
        if current == number:
            arr.remove(current)
            arr.remove(number)
            single_number(arr)
            return arr[0]
            break
        # else:
        #     return arr[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")