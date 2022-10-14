
Уровень 1

l = [1,4,1,6,'hello',"a",5, 'hello']
l_unique = []
for i in l:
    if i not in l_unique:
        l_unique.append(i)

print(l_unique)

print(list(set(l)))



Уровень 2

from random import *
 
n = 5
 
M = [] 
 
for i in range(1, n + 1):
    line = []  
    for j in range(1, n + 1):
        line = line + [randint(1, 100)]
    M = M + [line]
 
for i in range(0, n):
    for j in range(0, n):
        print(f" {M[i][j]:4d}", end="")
    print()
 
 
max_number = M[0][0]
 
for i in range(0,n):
    for j in range(0,n):
         
        if M[i][j] > max_number:
                max_number = M[i][j]
 
print("максимальное число = ", max_number)




Уровень 3

l = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
j = {}
for k, v in l.items():
    j[v] = k
print(j)





