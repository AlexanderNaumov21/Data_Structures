ctr = str(input("Введите вашу строку:"))
podctr = str(input("Введите слово, которое хотите найти:"))
ctr_len = len(ctr)
podctr_len = len(podctr)
chet1 = 0
chet2 = 0
bul = False

for i in range(ctr_len):
    if ctr[i] == podctr[chet2]:
        chet1 = chet1 + 1
        if chet1 == podctr_len:
            print("Слово найдено, индекс :", i)
            chet2  = 0
            chet1  = 0
            bul = True
            continue
        if ctr[i+1] != podctr[chet2+1]:
            i = i + 1
        chet2 = chet2 + 1
if bul == False:
    print("Подстрока не найдена.")