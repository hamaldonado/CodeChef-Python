# Contest Page: https://www.codechef.com/NOV21C/
#
# N = 5  (nodes)
# M = 10 (edges)
#
# primera parte: conectamos los N nodes usando los N-1 primeros edges
# --> (1,2) (2,3) (3,4) (4,5)
#
# segunda parte: con el resto de edges, vamos cerrando los nodos (en orden de menor a mayor), conectandoles los
# nodos que le toca recibir.  Notese que los primeros nodos de cada grupo ya se conectaron en la primera parte
# (marcados con *), por lo que esos no los consideramos
#
# 2 <- 1*                 2 recibe de 1              -->
# 3 <- 2*, 1              3 recibe de 2 y 1          --> (3,1)
# 4 <- 3*, 2, 1           4 recibe de 3, 2 y 1       --> (4,2) (4,1)
# 5 <- 4*, 3, 2, 1        5 recibe de 4, 3, 2 y 1    --> (5,3) (5,2) (5,1)
#
# La rpta entonces seria:
# --> (1,2) (2,3) (3,4) (4,5) (3,1) (4,2) (4,1) (5,3) (5,2) (5,1)

def solve(n, m):

    count = 0

    # first part: build the first N-1 bridges
    for i in range(1, n):
        print(str(i) + " " + str(i + 1))
        count += 1

    if count == m:
        return

    # second part: connect the nodes starting from the smaller ones
    for i in range(3, n + 1):

        for j in range(i - 2, 0, -1):
            print(str(i) + " " + str(j))
            count += 1

            if count == m:
                return



if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        input_line = input().split(" ")

        n = int(input_line[0])
        m = int(input_line[1])

        solve(n, m)




