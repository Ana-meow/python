# перевод времени, данного в секундах, в часы, минуты, секунды
# var - время в секундах, введённое пользователем
var = int(input("Введите время в секундах:"))
# выделение часов (h), как целое от деления секунд на 3600
h = var // 3600
# присвоение переменной остатка от деления
var = var % 3600
# выделение минут (m), как целое от деления секунд на 60
m = var // 60
# определение секунд (s), как остаток от деления
s = var % 60
print(f"{h:02}:{m:02}:{s:02}")
