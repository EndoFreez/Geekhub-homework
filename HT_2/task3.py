# Write a script which accepts a <number> from user and print out a sum
# of the first <number> positive integers.

sum_of = int(input("Number: "))
if sum_of >= 1:
	print(int(sum_of * (sum_of + 1) / 2))
else:
	print(None)
	