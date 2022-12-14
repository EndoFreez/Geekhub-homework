# 2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та
# кількість символів. Файл також додайте в репозиторій. На екран має 
# бути виведений список із трьома блоками - символи з початку, із 
# середини та з кінця файлу. Кількість символів в блоках - та, яка
# введена в другому параметрі. Придумайте самі, як обробляти помилку,
# наприклад, коли кількість символів більша, ніж є в файлі або, 
# наприклад, файл із двох символів і треба вивести по одному символу,
# то що виводити на місці середнього блоку символів?). Не забудьте
# додати перевірку чи файл існує.


def blocks(path, num):

    try:
        with open(path, 'r') as i:
            text = i.read()
            if num == 0:
                return print(text)
            if num < 0 and len(text) >= -num:
                text = text[::-1]
                num = -num
                start = text[0:num]
                mid = text[(len(text) - num) // 2:(len(text) + num) // 2]
                end = text[-num:]
                return print(start, mid, end)
            if len(text) >= num:
                start = text[0:num]
                mid = text[(len(text) - num) // 2:(len(text) + num) // 2]
                end = text[-num:]
                return print(start, mid, end)
            else:
                return print("Your file is shorter than your option")
    except ZeroDivisionError:
        print("Can't use Zero")
    except FileNotFoundError:
        print(f"File {path} not found")

if __name__ == "__main__":
    blocks("task_2.txt", -5), blocks("task_2.txt", 5)
