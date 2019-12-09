def merge(a, b):
    c = []
    iend = False
    jend = False
    i = 0
    j = 0
    while not(iend and jend):
        if iend:
            c.append(b[j])
            if j == (len(b) - 1):
                jend = True
            else:
                j += 1
        elif jend:
            c.append(a[i])
            if i == (len(a) - 1):
                iend = True
            else:
                i += 1
        else:
            if a[i] < b[j]:
                c.append(a[i])
                if i == (len(a) - 1):
                    iend = True
                else:
                    i += 1
            if a[i] > b[j]:
                c.append(b[j])
                if j == (len(b) - 1):
                    jend = True
                else:
                    j += 1
            if a[i] == b[j]:
                c.append(a[i])
                c.append(b[j])
                if j == (len(b) - 1):
                    jend = True
                else:
                    j += 1
                if i == (len(a) - 1):
                    iend = True
                else:
                    i += 1
    return c


x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(*merge(x, y))
