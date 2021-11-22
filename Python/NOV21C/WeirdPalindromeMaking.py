# Contest Page: https://www.codechef.com/NOV21C/

def minOperations(size, counts):

    num_odds = 0

    for number in counts:
        if number % 2 != 0:
            num_odds += 1

    if num_odds <= 1:
        return 0

    return num_odds // 2


if __name__ == "__main__":

    t = int(input())

    for _ in range(0, t):

        alphabet_size = int(input())
        alphabet_counts = [int(x) for x in input().split(" ")]

        print(minOperations(alphabet_size, alphabet_counts))
