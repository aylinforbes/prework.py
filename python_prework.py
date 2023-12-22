
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """ Display a simple greeting """
    user_name = input("What is your username?")
    print("hello_" + user_name + "!")
hello_name("user_name")

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """ Print all odd numbers from 1-100 """
    first_odds = 0
    while first_odds < 100:
        first_odds += 1
        if first_odds % 2 == 0:
            continue
        print(first_odds)
first_odds()


 #Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
a_list = [14, 4, 74, 21, 38, 52]
def max_num_in_list(a_list):
        """ define max number in list """
        print(max(a_list))  #automatically produces a return
max_num_in_list(a_list)
               

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
a_year = 2024
def is_leap_year(a_year):
    """ Define given number is a leap year"""
    if ((a_year % 400 == 0) or (a_year % 100 != 0) and (a_year % 4 == 0)):
        print("True")
    else:
        print("False")

is_leap_year(a_year)
   


               

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
a_list = [4, 2, 7, 3, 1] 
def is_consecutive(a_list):
      """ Check list for cosecutive numbers"""
      return sorted(a_list) == list(range(min(a_list), max(a_list)+1)) 
print(is_consecutive(a_list))
is_consecutive(a_list)


              

