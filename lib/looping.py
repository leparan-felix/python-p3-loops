#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
    # code goes here!
    pass

def square_integers(int_list):
    count = 0
    while count < len(int_list):
        int_list[count] = int_list[count] ** 2
        count += 1
    return int_list

    # code goes here!
    pass

def fizzbuzz():
    count = 1
    while count <= 100:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)
        count += 1
        
    # code goes here!
    pass
