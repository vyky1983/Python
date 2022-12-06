# n,m=map(int,input().split())
# matrix=[list(map(int,input().split())) for i in range(n)]
# for i in range(n):
#     print(*reversed(matrix[i]))

n,m = map(int, input().split())
lst = []
for i in range(n):
    a = []
    for _ in range(m):
        a.append(int(input()))
    lst.append(a)
print(lst)