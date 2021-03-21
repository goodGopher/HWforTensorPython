"""Realize unoptimized typical Fizz-Buzz exercise."""

def fizz_buzz(num):
    """Prints numbers from 1 to num or Fizz, Buzz and FizzBuzz.

    Argument:
        num --- the max integer number which we check and print.

    Basically print numbers from 1 to num.
    Prints Fizz instead of number if number divide without remainder by 3.  
    Prints Buzz instead of number if number divide without remainder by 5.  
    Prints FizzBuzz instead of number if number divide without remainder by 15.  

    """
    for i in range(1,num+1):
        if i % 15 == 0:
            print("Fizz" + "Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    n = input("Введите верхнюю границу диапазона чисел:")
    n = int(n)
    fizz_buzz(n)
    
        
