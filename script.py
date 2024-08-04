#Sorting-programm


def input_numbers():
	numbers = []

	while s := input():
		numbers.append(int(s))

	return numbers


def output_numbers(numbers):
	print(', '.join(map(str, numbers)))


data = input_numbers()
data = sorted(data)
output_numbers(data)
