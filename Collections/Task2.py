# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random
import string
from collections import defaultdict

list_of_dicts = []  # initialization of variable to collect generated dictionaries
number_of_dicts = random.randint(3, 10)  # initialization and generation random value to variable for number of


# def dict_sort(my_dict: dict):  # function that gets dict as argument and return sorted dict
#     my_keys = list(my_dict.keys())
#     my_keys.sort()
#     return {i: my_dict[i] for i in my_keys}

def dict_sort(my_dict: dict):
    return dict(sorted(my_dict.items()))


# while loop was selected because of by using for loop may cause loss duplicates of keys f.e. if generated value for
# amount of keys was 26, and we will have duplicates in keys value (2 times 'a' char) - we will have fewer keys in total
while True:  # Loop for filling in list by dicts
    this_dict = {}  # initialization temp dict variable to collect generated values
    number_of_pairs_in_dict = random.randint(3, 26)  # initialization and generating value for number of pairs in dict
    while True:  # Loop for filling in the dict
        this_dict[random.choices(string.ascii_lowercase)[0]] = random.randint(0, 100)  # adding random char as
        # a key and random int in range 0-100 as a pair into the dict
        if len(this_dict) == number_of_pairs_in_dict:  # Check if required amount of keys are already generated
            break  # Closing the loop filling the dict
    this_dict = dict_sort(this_dict)  # Sorting generated dict by function dict_sort
    list_of_dicts.append(this_dict)  # Adding generated dict to the list of dicts

    if len(list_of_dicts) >= number_of_dicts:  # Check length of list with dicts is less than required
        break  # break for loop when list will be filled up appropriate count times
for current_dict in list_of_dicts:      # print to console all the dicts separately
    print(current_dict)

# Task 2 part 2
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.

# Using defaultdict to get dict with all the keys and list of all value for this key
# It was used to find elements, that has the greatest values at first appearance to not to loose the data
dict_with_all_values = defaultdict(list)
for sub_dict in list_of_dicts:      # Iterate threw the list of dicts
    for key in sub_dict:            # Iterate threw the keys of iterated dict
        dict_with_all_values[key].append(sub_dict[key])     # append value of the key to existed or created key


new_dict = {}  # Initialization new dict variable
dict_for_changed_elements = {}  # Initialization dict variable for changed elements (key = key, value = dict number)


for number_of_dict in range(len(list_of_dicts)):  # Loop for detecting duplicates in keys
    list_of_keys_in_current_dict = list(list_of_dicts[number_of_dict])  # initialization variable to hold list of dicts
    current_dict = list_of_dicts[number_of_dict]  # initialization temporary variable holding current dictionary
    keys_for_current_dict = list(current_dict.keys())  # initialization temporary variable to hold keys of current dict
    for key_number in range(len(list_of_keys_in_current_dict)):  # loop for filling in new_dict with all values
        # dict_for_changed_elements_flags[keys_for_current_dict[key_number]] = 0
        if list_of_keys_in_current_dict[key_number] in new_dict:  # check for presence of the key in the common dict
            if list_of_dicts[number_of_dict][list_of_keys_in_current_dict[key_number]] > new_dict[list_of_keys_in_current_dict[key_number]]:  #
                # check for bigger value to that key
                new_dict[list_of_keys_in_current_dict[key_number]] = list_of_dicts[number_of_dict][list_of_keys_in_current_dict[key_number]]  #
                # adding value to new_dick
                dict_for_changed_elements[keys_for_current_dict[key_number]] = number_of_dict + 1  # adding dict number to proper dict
                # dict_for_changed_elements_flags[keys_for_current_dict[key_number]] += 1
        else:
            new_dict[list_of_keys_in_current_dict[key_number]] = list_of_dicts[number_of_dict][list_of_keys_in_current_dict[key_number]]  # adding
            # if key has more than one appearance in all dicts
            if len(dict_with_all_values[list_of_keys_in_current_dict[key_number]]) != 1:
                # add dict number to the special dict
                dict_for_changed_elements[keys_for_current_dict[key_number]] = number_of_dict + 1

print(new_dict)

new_final_dict = {}  # dict variable for items with proper key names
keys_for_new_dict = list(new_dict.keys())  # variable initialization with list of keys from new_dict
keys_for_dict_for_changed_elements = list(dict_for_changed_elements.keys())  # variable initialization with list
# keys_from_dict_for_changed_elements_flags = list(dict_for_changed_elements_flags.keys())
# of keys from dict_for_changed_elements
for key_number in range(len(new_dict)):  # loop for creating dict with proper keys
    if keys_for_new_dict[key_number] in dict_for_changed_elements:  # check if key is present in dict for keys should be changed
        new_final_dict[str(keys_for_new_dict[key_number]) + "_" + str(dict_for_changed_elements[keys_for_new_dict[key_number]])] = new_dict[keys_for_new_dict[key_number]]  #
        # adding key-value pair with proper key name and max value
    else:
        new_final_dict[keys_for_new_dict[key_number]] = new_dict[keys_for_new_dict[key_number]]  # adding key-value pair with unchanged
        # key and value

new_final_dict = dict_sort(new_final_dict)  # sorting final dict
print(new_final_dict)  # print final result - can be deleted

