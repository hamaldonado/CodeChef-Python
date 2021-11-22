# Contest Page: https://www.codechef.com/NOV21C/

def whichFuelCostsLess(x, y, a, b, k):

    petrol = x + a * k
    diesel = y + b * k

    if petrol < diesel:
        return "PETROL"
    elif petrol > diesel:
        return "DIESEL"

    return "SAME PRICE"


if __name__ == "__main__":

    t = int(input())

    for _ in range(0, t):

        test_case = [int(x) for x in input().split(" ")]

        x = test_case[0]
        y = test_case[1]
        a = test_case[2]
        b = test_case[3]
        k = test_case[4]

        print(whichFuelCostsLess(x, y, a, b, k))
