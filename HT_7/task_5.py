# 5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість
# окремих регістро-незалежних букв та цифр, які зустрічаються в рядку
# більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих
# і малих). Реалізуйте обчислення за допомогою генератора в один рядок
#    Example (input string -> result):
#    "abcde" -> 0            # немає символів, що повторюються
#    "aabbcde" -> 2          # 'a' та 'b'
#    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#    "indivisibility" -> 1   # 'i' присутнє 6 разів
#    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#    "aA11" -> 2             # 'a' і '1'
#    "ABBA" -> 2             # 'A' і 'B' кожна двічі


def repeat_char(some_string):
    return len(set(char for char in some_string.lower() if some_string.lower().count(char) > 1))


input_string = input("Input string: ")
print(f'{input_string} --> {repeat_char(input_string)}')