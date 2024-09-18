def is_even(digit):
    valide_last_digits = [0, 2, 4, 6, 8]
    list_of_digits = list(str(digit))
    last_digit = int(list_of_digits[-1])
    result = False
    if last_digit in valide_last_digits:
        result = True
    return result

def is_even(digit):
    valide_last_digit = [0, 2, 4, 6, 8]
    lst = list(str(digit))
    return int(lst[-1]) in valide_last_digit
    # Або такий варіант, тоді не доведеться створювати змінну lst
    # але код стає менш читабельним
    # return int(list(str(digit))[-1]) in valide_last_digit


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Усі тести успішно пройдені!')
