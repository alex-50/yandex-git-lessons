#Sorting-programm


def input_numbers():
	return [int(number) for number in input().split()]


def output_numbers(numbers):
	print(', '.join(map(str, numbers)))


data = input_numbers()
data = sorted(data)
output_numbers(data)
