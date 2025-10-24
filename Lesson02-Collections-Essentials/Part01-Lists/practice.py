def filter_evens(numbers):
    number_list = []
    for number in numbers:
        if number % 2 == 0:
            number_list.append(number)
    return number_list
result = filter_evens([1, 2, 3, 4, 5, 6])
print(result)
result = filter_evens([10, 15, 20, 25])
print(result)
result = filter_evens([1, 3, 5])
print(result)