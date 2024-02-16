x = int(input("Insira um número para saber sua fatorial: "))
fat = 1
for y in range(x, 0, -1):
    fat = fat * y
print(fat)