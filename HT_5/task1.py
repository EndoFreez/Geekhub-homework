# 1. Написати функцію <square>, яка прийматиме один аргумент - сторону
# квадрата, і вертатиме 3 значення у вигляді кортежа: периметр 
# квадрата, площа квадрата та його діагональ.

def square(a):
	per = a * 4
	sq = a ** 2
	diag = 2 ** 0.5 * a
	return (per, sq, diag)


a = float(input("Сторона квадрату: "))
print(square(a))