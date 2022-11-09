def factorial(n): # TODO запишите здесь функцию factorial
    result = 1
    for num in range(1, n + 1):
        result *= num

    return result

print(factorial(5)) # TODO распечатать результат выполнения функции factorial от числа 5

