print("=== Профиль Python-разработчика ===")
name = input("Введите имя: ")
city = input("Введите город: ")
topic = input("Любимая тема Python: ")


try:
    projects = int(input("Сколько проектов вы создали? "))
    print("----- Профиль -----")
    print(f"Имя: {name}")
    print(f"Город: {city}")
    print(f"Количество проектов : {projects}")
    print(f"Любимая тема: {topic}")
    print("-------------------")

    if projects == 0:
        print("Первый проект уже скоро появится!")
    if projects <=1 and projects <= 3:
        print("Ты уже создал(а) несколько проектов — впереди backend-разработка!")
    if projects >= 4:
        print("Отличный опыт! Пора осваивать инструменты профессионального разработчика.")

except ValueError:
    print("Ошибка: количество проектов нужно вводить цифрами.")

