# Digant Kumar

# Syracuse Sequence / Collatz Sequence
# Returns n//2 if the user enters a positive even number and 3*n+1 if the user enters a positive odd number
def syracuse_fn(n):
    if n<0:
        n = int(input("Enter a positive number: "))
    if n == 1:
        return 1
    if n%2 == 0:
        return n//2
    elif n%2 == 1:
        return 3*n + 1

# Returns the largest element of the sequence and its length
def syracuse_seq(n):
    num = syracuse_fn(n)
    largest = num
    length = 1
    while num != 1:
        length += 1
        if num > largest:
            largest = num
        num = syracuse_fn(num)
    length += 1
    return length,largest

# Returns the longest sequence for starting points and up to and including n.
def longest_seq(n):
    highest_length = 1
    start_point = 1
    for i in range(1,n+1):
        num = syracuse_seq(i)
        if highest_length < num[0]:
            highest_length = num[0]
            start_point = i
    return start_point, highest_length
