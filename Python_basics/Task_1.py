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

odd_sum = 0  # Initialization of the int variable to collect sum of odd elements in my_list
even_sum = 0  # Initialization of the int variable to collect sum of even elements in my_list

for i in range(len(my_list)):  # Starting a loop that will go threw all the elements in my_list
    if i % 2 == 0:  # Check if selected element is odd
        odd_sum += my_list[i]  # Summing up value of the element to odd_sum variable
    else:  # Otherwise ( if selected element is even)
        even_sum += my_list[i]  # Summing up value of the element to even_sum variable

odd_average = odd_sum / (len(my_list) / 2)  # Calculating average value of odd elements
even_average = even_sum / (len(my_list) / 2)  # Calculating average value of even elements

# Printing results
print("Odd numbers average : " + str(odd_average))
print("Even numbers average : " + str(even_average))

