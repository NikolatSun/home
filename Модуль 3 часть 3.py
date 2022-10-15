
# Уровень 1

a = int(input())  
b = int(input())
c = int(input())
p = (a + b + c) / 2  
s = (p * (p - a) * (p - b) * (p - c))**0.5   
print (s)



Уровень 2


s = "'vVv', 'Снег', 'Самолет', 'Санки', 'Gleb'"
print([i for i in eval('('+s+')') if len(i)<5])






