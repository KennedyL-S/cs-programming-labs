def print_table_2(name, f1, f2):
    print(f"Равносильность: {name}")
    print("Таблица истинности:")
    print("+---+---+---------+---------+")
    print("| x | y | f(x, y) | g(x, y) |")
    print("+---+---+---------+---------+")
    for x in (0, 1):
        for y in (0, 1):
            v1 = int(f1(x, y))
            v2 = int(f2(x, y))
            print(f"| {x} | {y} |    {v1}    |    {v2}    |")
    print("+---+---+---------+---------+\n")

def print_table_3(name, f1, f2):
    print(f"Равносильность: {name}")
    print("Таблица истинности:")
    print("+---+---+---+------------+------------+")
    print("| x | y | z | f(x, y, z) | g(x, y, z) |")
    print("+---+---+---+------------+------------+")
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                v1 = int(f1(x, y, z))
                v2 = int(f2(x, y, z))
                print(f"| {x} | {y} | {z} |      {v1}     |      {v2}     |")
    print("+---+---+---+------------+------------+\n")

# 1. Формула замены импликации (x -> y = not x or y)
print_table_2("формула замены импликации",
              lambda x, y: not x or y,
              lambda x, y: not x or y)

# 2. Закон контрапозиции
print_table_2("закон контрапозиции",
              lambda x, y: not x or y,
              lambda x, y: not (not y) or (not x))

# 3. Законы де Моргана (1)
print_table_2("первый закон де Моргана",
              lambda x, y: not (x and y),
              lambda x, y: not x or not y)

# 4. Законы де Моргана (2)
print_table_2("второй закон де Моргана",
              lambda x, y: not (x or y),
              lambda x, y: not x and not y)

# 5. Первый закон дистрибутивности
print_table_3("первый закон дистрибутивности",
              lambda x, y, z: x and (y or z),
              lambda x, y, z: (x and y) or (x and z))

# 6. Второй закон дистрибутивности
print_table_3("второй закон дистрибутивности",
              lambda x, y, z: x or (y and z),
              lambda x, y, z: (x or y) and (x or z))

# 7. Законы поглощения (1)
print_table_2("первый закон поглощения",
              lambda x, y: x or (x and y),
              lambda x, y: x)

# 8. Законы поглощения (2)
print_table_2("второй закон поглощения",
              lambda x, y: x and (x or y),
              lambda x, y: x)

# 9. Законы склеивания (1)
print_table_2("первый закон склеивания",
              lambda x, y: (x and y) or (x and not y),
              lambda x, y: x)

# 10. Законы склеивания (2)
print_table_2("второй закон склеивания",
              lambda x, y: (x or y) and (x or not y),
              lambda x, y: x)

# 11. Законы сокращения (1)
print_table_2("первый закон сокращения",
              lambda x, y: x or (not x and y),
              lambda x, y: x or y)

# 12. Законы сокращения (2)
print_table_2("второй закон сокращения",
              lambda x, y: x and (not x or y),
              lambda x, y: x and y)