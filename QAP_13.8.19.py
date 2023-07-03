N = int(input("Введите количество билетов: "))
if N>=100 or N<=0:
    print("Введено некорректное количество билетов")
else:
    i=1
    result=0

    while i <= N:
        try:
            age = int(input(f"{i}) Введите возраст человека: "))
            if age >100 or age <=0:
                raise ValueError("Некорректный возраст!")
        except ValueError:
            print("Неправильный возраст")
            continue

        if 0<age<18:
            result+=0
        elif 18<=age<25:
            result+=990
        elif age>=25:
            result+=1390
        i+=1

    if not result:
        print("Билеты для поситителей до 18-ти лет бесплатны")
        print("Итого к оплате: ", result, "руб.")
    else:
        if N>3:
            result=result*0.9
            print("Для группы более 3-х человек предоставлена скидка 10%")
            print("Итого к оплате: ", result, "руб.")
        else:
            print("Итого: ", result, "руб.")
