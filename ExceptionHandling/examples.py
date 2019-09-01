# def factorial(n):
# 	# n! can also be defined as n * (n-1)!
# 	if n <= 1:
# 		return 1
# 	else:
# 		return n * factorial(n-1)
#
#
# try:
# 	print(factorial(900))
# except (RecursionError, ZeroDivisionError):
# 	print("This program cannot calculate factorials that large")
#
# print("Program terminating")


def divide(a, b):
	print(a / b)


try:
	num1 = int(input("Please enter a number: "))
	num2 = int(input("Please enter a second number: "))
except ValueError:
	print("invalid input")


try:
	divide(num1, num2)
except ZeroDivisionError:
	print("can't divide by zero")

