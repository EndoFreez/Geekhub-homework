# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# - якесь власне додаткове правило :)
# Якщо якийсь із параметрів не відповідає вимогам - породити виключення
# із відповідним текстом.class LoginException(Exception):
#  pass

class LoginException(Exception):
    pass

def login_pass(username, password):

    if 3 >= len(username) < 50:
        raise LoginException(">3<50")
    if len(password) < 8:
        raise LoginException("Має бути 8 або більше символів у паролі!")
    if not any(i.isdigit() for i in password):
        raise LoginException("Пароль має містити цифри")
    if not any(i.isupper() for i in password):
        raise LoginException("Пароль має містити великі літери")
    else:
        return print("Хух, ви це зробили, вітаю!!!")


login_pass("Kodfsdf", "asdas3434SDSDfdg")
login_pass("Kovbasar1", "Kosalsjd123")
login_pass("Koererer", "sobaka123")
