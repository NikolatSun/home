from random import randint
 

a = []
for i in range(15):
    a.append(randint(1, 50))
a.sort()
print(a)

value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1
 
while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print("No value")
else:
    print("ID =", mid)



a = [4, 5, 6, 10, 1, 3]

def insertion_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i- 1):
            if a[j] > a[j + 1]:
                a[j], a[j +1] = a[j +1], a[j]
    return a 

print(a)
print(insertion_sort(a))



graph = {'0': set(['1', '2']),
'1': set(['0', '3', '4']),
'2': set(['0']),
'3': set(['1']),
'4': set(['2', '3'])}

def bfs(graph, start, visited = []):
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            visited = bfs(graph, v, visited)
    return visited

print(bfs(graph, '3'))