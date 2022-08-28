import sys


def find_path(n,m,a):
    
    INF = 10 ** 20
    C = [[0] * (m ) for i in range(n)]
    C[0][0] = 0

    for i in range(0, n ):
        C[i][0] = INF
    for j in range(0, m ):
        C[0][j] = INF

    for i in range(0, n):
        for j in range(0, m):
            if i ==0:
                C[i][j] = C[i][j - 1] + a[i][j]
            elif j == 0:
                C[i][j] = C[i - 1][j] + a[i][j]
            else:
                C[i][j] = min(C[i][j - 1], C[i - 1][j]) + a[i][j]
    Answer = []
    
    i = n-1
    j = m-1
    while (i,j) > (0,0):

        Answer.append((i, j))
        if i ==0:
            prev_C = C[i][j - 1]
            if C[i][j - 1] == prev_C:
                i, j = i, j - 1
        elif j ==0:
            prev_C = C[i-1][j]
            if C[i - 1][j] == prev_C:
                i, j = i - 1, j
        else:
            prev_C = min(C[i][j - 1], C[i - 1][j])
            if C[i][j - 1] == prev_C:
                i, j = i, j - 1
            elif C[i - 1][j] == prev_C:
                i, j = i - 1, j
    if a[0][0] == 1:
        Answer.append((0, 0))
    res = 0
    for i in Answer:
        res += a[i[0]][i[1]]
    print(res)


def main():
    map_d = {
    '.': 0,
    '#': 1
    }
    
    input_string1 = list(map(int, sys.stdin.readline().split()))
    n = input_string1[0]
    m = input_string1[1]
    
    a = []
    for row in range(n):
        new_row = []
        inp_row = sys.stdin.readline().strip()
        for letter in inp_row:
            new_row.append(map_d[letter])
        a.append(new_row)
        
    find_path(n, m, a)
    

if __name__ == "__main__":
    main()