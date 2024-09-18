def prime_generator(end):
    for i in range (2, end+1):
        divisors = 0
        for j in range (2, end+1):
            if i%j == 0:
                divisors += 1
        if divisors == 1:
            yield i



from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')