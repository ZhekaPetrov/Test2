# Test2

# Write a program that reads three numbers and calculates the sum of only positive numbers.
# Напишите программу, которая считывает три числа и вычисляет сумму только положительных чисел.

a = int(input())
b = int(input())
c = int(input())
if a >= 0 and b >= 0 and c >= 0:
    print(a + b + c)
elif a <= 0 and b >= 0 and c >= 0:
    print(b + c)
elif a >= 0 and b <= 0 and c >= 0:
    print(a + c)
elif a >= 0 and b >= 0 and c <= 0:
    print(a + b)
elif a <= 0 and b <= 0 and c >= 0:
    print(c)
elif a >= 0 and b <= 0 and c <= 0:
    print(a)
elif a <= 0 and b >= 0 and c <=0:
    print(b)
elif a < 0 and b < 0 and c < 0:
    print("0")
    
#A shorter solution
#Более короткое решение

a = int(input())
b = int(input())
c = int(input())
num = 0
if a > 0:
    num += a # (num += a) == (num = num + a)
if b > 0:
    num += b
if c > 0:
    num += c
print(num)

