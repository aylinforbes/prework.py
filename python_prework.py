
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name)
hello_name("USERNAME!")

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    first_odds = 0
    while first_odds<100:
        first_odds += 1
        if first_odds % 2 == 0:
            continue
        print(first_odds)
first_odds()


 #Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    a_list = [14, 4, 74, 21, 38, 52]
    print(max(a_list))
max_num_in_list("a_list")
               

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

a_year = int(input("Enter a year: "))
if is_leap_year(a_year):
    print(bool(a_year))
else:
    print(bool(a_year))


               

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
      return sorted(a_list) == list(range(min(a_list), max(a_list)+1)) 
a_list = [4, 2, 5, 3, 1]  
print(is_consecutive(a_list))          

              

