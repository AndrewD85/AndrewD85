import random
list = [random.randint(1,1000) for i in range(20)]
print(list)
a = int(input("Введите число от 0 до 19:"))
list[a] = a
print(list)
