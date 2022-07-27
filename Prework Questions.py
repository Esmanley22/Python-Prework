#Question 1

def hello_name(user_name):
    user_name = input(f"What is your USERNAME?")
    print("Hello" + " " + user_name.upper() + "!")
hello_name('user_name')


#Question 2
def odd_numbers():
    for h in range(1,101,2):
        print(h)
odd_numbers()
        


#Question 3

def max_num_in_list(a_list):

    a_list = [4000, 2, 300, 4, 21397, 6, 7, 8, 9, 10, 11, 12 ,27, 14, 15, 24, 17, 18, 20, 19]

    a_list.sort()

    print(a_list[-1])
max_num_in_list(a_list)



#Question 4

def is_leap_year(a_year):
    (a_year)= int(input("Put a year here" + " " + "=> "))
    if (a_year % 4) == 0:
        if (a_year % 100) == 0:
            if (a_year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
is_leap_year(a_year)


#Question 5

def is_consecutive(a_list):
    a_list = [1,2,3]
    x = 0
    status = True
    while x < len(a_list) - 1:
       if a_list[x] + 1 == a_list[x + 1]:
           x += 1
       else:
            status = False
            break
    print(status)
is_consecutive(a_list)


