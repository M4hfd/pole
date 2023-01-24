words = []
secretword = input("Введите секретное слово: ")
words.append(secretword)
print()
print("\033[2J")
win = False
list = []
true_letters = []
points = [0, 0, 0]
counter = 1

while win == False:
    letter = input("\nИгрок " + str(counter) + " введите букву: ")  
    if letter in list:
        print("Буква " + letter + " уже была названа")
    elif letter in secretword:
        print("Вы угадали букву: " + letter)
        true_letters.append(letter)
        if counter == 1:
            points[0] += 1
            print("Счет: " + str(points[0]))
        if counter == 2:
            points[1] += 1
            print("Счет: " + str(points[1]))
        if counter == 3:
            points[2] += 1
            print("Счет: " + str(points[2]))
    else:
        print("Буквы " + letter +  " нет в слове")
    list.append(letter)
    for symbol in secretword:
        if symbol in true_letters:
           print(symbol, end="")
        else:
            print("*", end="")
    if counter == 1 or 2:
        counter += 1
    if counter == 4:
        counter -= 3
    if set(true_letters) == set(secretword):
        win = True
        print("\nСчет игроков: \n Игрок 1: " + str(points[0]) + "\n Игрок 2: " + str(points[1]) + "\n Игрок 3: " + str(points[2]))

