# Задайте натуральное число N. 
# Напишите программу, которая 
# составит список простых 
# множителей числа N.


def prime_factorization(n):
   d = 2
   divisors = {}
   while n > 1:
       if n % d == 0:
           divisors[d] = divisors.get(d, 0) + 1
           n //= d
       elif d*d > n:
           d = n
       else:
           d += 1
   return divisors
if __name__ == '__main__':
   n = int(input('Задайте натуральное число : '))
   factors = prime_factorization(n)
   itog = ' * '.join([f'число [{k}] повторяется {v} раз' for k, v in sorted(factors.items())])
   print(itog)
   

