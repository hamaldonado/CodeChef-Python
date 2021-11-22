# Contest Page: https://www.codechef.com/NOV21C/

import io
import os
import time


# Function to take normal input
def normal_io():
    # Stores the start time
    start = time.perf_counter()

    # Take Input
    s = input().strip();

    # Stores the end time
    end = time.perf_counter()

    # Print the time taken
    print("\nTime taken in Normal I / O:", end - start)


# Function for Fast Input
def fast_io():
    # Reinitialize the Input function
    # to take input from the Byte Like
    # objects
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    # Fast Input / Output
    start = time.perf_counter()

    # Taking input as string
    s = input().decode()

    # Stores the end time
    end = time.perf_counter()

    # Print the time taken
    print("\nTime taken in Fast I / O:", \
          end - start)

def XorEquation(n_size, n):

    xor_acum = 0
    result = -1
    max = 0

    for num in n:
        if num > max:
            max = num

        xor_acum ^= num

    if xor_acum % n_size == 0:

        sum = xor_acum // n_size

        if max.bit_length() == (max + sum).bit_length():
            result = sum

    return result

if __name__ == "__main__":
    t = int(input())

    n_size = 0
    n = []

    for _ in range(t):

        n_size = int(input())
        s = input()

        n = [int(x) for x in s.split(" ")]

        print(XorEquation(n_size, n))

