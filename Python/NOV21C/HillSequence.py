# Contest Page: https://www.codechef.com/NOV21C/

def hillSequence(arr_size, arr):

    if arr_size == 1:
        return arr

    arr.sort(reverse=True)
    count = 1

    if arr[0] == arr[1]:    # The max value cannot be repeated
        return -1

    if arr_size == 2:
        return arr

    for i in range(2, arr_size):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1

        if count == 2:    # if an item is duplicated move one copy to the front of arr
            temp = arr[i - 1]
            arr.pop(i - 1)
            arr.insert(0, temp)

        if count == 3:    # if an item is triplicated, the problem cannot be solved
            return -1

    return arr

if __name__ == "__main__":

    t = int(input())

    for _ in range(0, t):

        arr_size = int(input())
        arr = [int(x) for x in input().split(" ")]

        result = hillSequence(arr_size, arr)

        if isinstance(result, list):
            print(" ".join([str(x) for x in result]))
        else:
            print(result)
