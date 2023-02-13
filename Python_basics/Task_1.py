# Importing random module
import random

my_list = []  # Creating of an empty array

for i in range(100):  # Starting a loop that will work for 100 times
    my_list.append(random.randint(0, 1000))  # append random int in range 0 - 1000 to my_list array
print(len(my_list))
for i in range(len(my_list) - 1):  # Starting a loop for bubble sort
    for j in range(len(my_list) - i - 1):  # Starting loop in the loop for bubble sort
        if my_list[j] > my_list[j + 1]:  # Check if selected item is bigger that next one
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[
                j]  # Replacing the positions of neighboring elements

odd_summ = 0        # Initialization of the int variable to collect summ of odd elements in my_list
odd_counter = 0     # Initialization of the int variable to collect amount of add elements in my list
even_summ = 0       # Initialization of the int variable to collect summ of even elements in my_list
even_counter = 0    # Initialization of the int variable to collect amount of even elements in my list
for i in range(len(my_list)):  # Starting a loop that will go threw all the elements in my_list
    if my_list[i] % 2 == 0:  # Check if selected element is odd
        odd_summ += my_list[i]  # Summing up value of the element to odd_summ variable
        odd_counter += 1        # increasing counter for odd elements
    else:  # Otherwise ( if selected element is even)
        even_summ += my_list[i]  # Summing up value of the element to even_summ variable
        even_counter += 1       # increasing counter for even elements

odd_average = odd_summ / odd_counter  # Calculating average value of odd elements
even_average = even_summ / even_counter  # Calculating average value of even elements

# Printing results
print("Odd numbers average : " + str(odd_average))
print("Even numbers average : " + str(even_average))

