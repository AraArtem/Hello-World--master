def get_list_number_divisors(number):
      # TODO найти список делителей числа number
    list_divisor = []
    for divisor in range(1, number+1):
        if number % divisor == 0:
            list_divisor.append(divisor) == 0

    return list_divisor

print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))


