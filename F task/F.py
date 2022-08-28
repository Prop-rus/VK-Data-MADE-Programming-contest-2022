import sys


def find_min(n, m, T, t):
    
    t.sort()
    zak_num = 0
    zak = []
    i = 1
    zak_len = 1
    zak_min = t[0] + T
    while i < n:
        if t[i] > zak_min or zak_len == m:
            zak_num += 1
            zak = []
            zak_len = 1
            zak_min = t[i] + T
        else:
            zak_len += 1
            if t[i] + T < zak_min:
                zak_min = t[i] + T
        if i == n-1:
            zak_num += 1
        i += 1
    print(zak_num)


def main():
    
    input_string1 = list(map(int, sys.stdin.readline().split()))
    n = input_string1[0]
    
    m = input_string1[1]
    T = input_string1[2]
    
    t = [0] * n
    for row in range(n):
        
        t[row] = int(sys.stdin.readline().strip())
    if n == 1:
        print(1)
        return
    
    find_min(n, m, T, t)


if __name__ == "__main__":
    main()