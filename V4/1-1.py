array1 = []
po = 0 
while True: 
    try: 
        for i in range(4):
            p = int(input("Введите число:"))
            if p in array1:
                po += 1
            array1.append(p)
        break
    except ValueError:
        print("Это не целые числа, повторите операцию с самого начала.")
        array1 = []

print("Получившийся список:", array1)

if po == 0:
    print("Нет повторов")
else:
    print("Есть повторы")

