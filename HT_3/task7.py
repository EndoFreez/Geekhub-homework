# Write a script which accepts a <number>(int) from user and generates
# dictionary in range <number> where key is <number> and value is 
# <number>*<number> e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

num = range(int(input("Num of keys: "))+1)
print({i: i ** 2 for i in num})