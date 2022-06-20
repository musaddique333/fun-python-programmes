import numpy as np
import os


if __name__ == '__main__':
    os.system("clear")
    print("Enter the number of rows\n")
    r = int(input())
    c = int(r * 2 - 1)
    a = np.zeros([r, c], int)
    a[0, int(c / 2)] = 1
    a[r - 1, c - 1] = 1
    for i in range(1, r):
        for j in range(c - 1):
            a[i, j] = a[i - 1, j - 1] + a[i - 1, j + 1]
    new = []
    for i in range(r):
        for j in range(c):
            new.append(a[i, j])
    new = list(map(str, new))
    for i in range(len(new)):
        if new[i] == '0':
            new[i] = ' '
    m = 0
    w = c
    for i in range(r):
        for j in range(m, w):
            print(new[j], end=" ")
        m = m + c
        w = w + c
        print("\n")
