# Contest Page: https://www.codechef.com/NOV21C/

def EqualCoins(x, y):
    total = x + 2 * y

    if total % 2 != 0:
        return "NO"

    resto = (total / 2) % 2

    if resto == 0 or x > resto:
        return "YES"

    return "NO"

if __name__ == "__main__":

    t = int(input())

    for _ in range(0, t):

        test_case = [int(x) for x in input().split(" ")]

        x = test_case[0]
        y = test_case[1]

        print(EqualCoins(x, y))
