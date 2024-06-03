def combine_coins(coin, numbers):
    return ', '.join([coin + str(num) for num in numbers])


print(combine_coins('$', range(5)))
import random;

p = lambda: random.choice('7♪♫♣♠♦♥◄☼☽');
[print('|'.join([p(), p(), p()]), end='\r') for i in range(8 ** 5)]
