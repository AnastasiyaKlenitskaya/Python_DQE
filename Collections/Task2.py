# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random
import string

list_of_dicts = []      # initialization of variable to collect generated dictionaries
number_of_dicts = random.randint(3, 10)     # initialization and generation random value to variable for number of
# generated dictionaries


def dict_sort(my_dict: dict) -> dict:       # function that gets dict as argument and return sorted dict
    my_keys = list(my_dict.keys())      # getting list of keys for given dict
    my_keys.sort()                      # sorting list of keys from the dict
    return {i: my_dict[i] for i in my_keys}     # returning dict with sorted keys


# while loop was selected because of by using for loop may cause loss duplicates of keys f.e. if generated value for
# amount of keys was 26, and we will have duplicates in keys value (2 times 'a' char) - we will have fewer keys in total
while True:          # Loop for filling in list by dicts
    this_dict = {}      # initialization temp dict variable to collect generated values
    number_of_pairs_in_dict = random.randint(3, 26)    # initialization and generating value for number of pairs in dict
    while True:        # Loop for filling in the dict
        this_dict[''.join(random.choices(string.ascii_lowercase))] = random.randint(0, 100)  # adding random char as
        # a key and random int in range 0-100 as a pair into the dict
        if len(this_dict) == number_of_pairs_in_dict:       # Check if required amount of keys are already generated
            break       # Closing the loop filling the dict
    this_dict = dict_sort(this_dict)    # Sorting generated dict by function dict_sort
    list_of_dicts.append(this_dict)     # Adding generated dict to the list of dicts

    if len(list_of_dicts) >= number_of_dicts:  # Check length of list with dicts is less than required
        break       # break for loop when list will be filled up appropriate count times

# Task 2 part 2
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.

new_dict = {}   # Initialization new dict variable
dict_for_changed_elements = {}      # Initialization dict variable for changed elements (key = key, value = dict number)
for x in range(len(list_of_dicts)):     # Loop for detecting duplicates in keys
    list_of_keys_in_current_dict = list(list_of_dicts[x])   # initialization variable to hold list of dicts
    current_dict = list_of_dicts[x]     # initialization temporary variable holding current dictionary
    keys_for_current_dict = list(current_dict.keys())   # initialization temporary variable to hold keys of current dict
    for y in range(len(list_of_keys_in_current_dict)):  # loop for filling in new_dict with all values
        if list_of_keys_in_current_dict[y] in new_dict:  # check for presence of the key in the dict
            if list_of_dicts[x][list_of_keys_in_current_dict[y]] > new_dict[list_of_keys_in_current_dict[y]]:   #
                # check for bigger value to that key
                new_dict[list_of_keys_in_current_dict[y]] = list_of_dicts[x][list_of_keys_in_current_dict[y]]   #
                # adding value to new_dick
                dict_for_changed_elements[keys_for_current_dict[y]] = x + 1     # adding dict number to proper dict
        else:
            new_dict[list_of_keys_in_current_dict[y]] = list_of_dicts[x][list_of_keys_in_current_dict[y]]  # adding
            # value to new_dick

new_final_dict = {}     # dict variable for items with proper key names
keys_for_new_dict = list(new_dict.keys())   # variable initialization with list of keys from new_dict
keys_for_dict_for_changed_elements = list(dict_for_changed_elements.keys())     # variable initialization with list
# of keys from dict_for_changed_elements
for x in range(len(new_dict)):      # loop for creating dict with proper keys
    if keys_for_new_dict[x] in dict_for_changed_elements:   # check if key is present in dict for keys should be changed
        new_final_dict[str(keys_for_new_dict[x]) + "_" + str(dict_for_changed_elements[keys_for_new_dict[x]])] = new_dict[keys_for_new_dict[x]]     #
        # adding key-value pair with proper key name and max value
    else:
        new_final_dict[keys_for_new_dict[x]] = new_dict[keys_for_new_dict[x]] # adding key-value pair with unchanged
        # key and value

new_final_dict = dict_sort(new_final_dict)      # sorting final dict
print(new_final_dict)   # print final result - can be deleted


