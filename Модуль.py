from random import randint
 

a = []
for i in range(11):
    a.append(randint(1, 66))
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







graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print (s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'A')


























