# Description
# homEwork: tHis iz your homeWork, copy these Text to variable.
#
# You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each
# existING SENtence and add it to the END OF this Paragraph.
#
#   it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
#
# last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I
# got 87.


string_value = 'homEwork:\n  tHis iz your homeWork, copy these Text to variable.\n\n  You NEED TO normalize it fROM ' \
               'letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING ' \
               'SENtence and add it to the END OF this Paragraph.\n\n  it iZ misspeLLing here. fix“iZ” with correct ' \
               '“is”, but ONLY when it Iz a mistAKE.\n\n  last iz TO calculate nuMber OF Whitespace characteRS' \
               ' in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.' \

counter = 0     # variable to count whitespaces
list_of_last_words = []     # variable to keep list of last words in sentences
flag_to_change_case = False     # flag to detect first word in sentence
new_string = ''     # variable to keep last words of each sentence

string_value = string_value.lower()     # converting string to lover case
string_value = string_value.capitalize()  # converting string to make first word capitalized
split_string = string_value.split()     # variable to keep list of words of the provided text

# normalizing string from letter case point of view
for x in range(len(string_value) - 2):
    # check flag and that current element is a char
    if flag_to_change_case and string_value[x].isalpha():
        # changing case of found char
        string_value = string_value[0:x] + string_value[x].swapcase() + string_value[x + 1: len(string_value)]
        flag_to_change_case = False            # changing back flag value
    if string_value[x] in ['.', '\n', '\t']:   # check to detect end of sentence to change flag value
        flag_to_change_case = True             # changing flag value

# detecting last words in each string
for x in range(len(split_string)):
    if split_string[x][len(split_string[x]) - 1] == '.':    # check if split word contains dot at the end
        if split_string[x][:len(split_string[x]) - 1].isalpha():  # check is the last split word consist of words
            list_of_last_words.append(split_string[x][:len(split_string[x]) - 1])   # adding word to list
        else:   # else - split word contains symbols instead of letters
            list_of_last_words.append(split_string[x - 1][:len(split_string[x])])   # adding previous word to the list


# creating new string with last words of each sentence
for x in range(len(list_of_last_words)):
    new_string += list_of_last_words[x]     # adding word to new string
    if x != (len(list_of_last_words) - 1):  # if added word was not last in list
        new_string += ' '                   # add space after added word
    else:                                   # else (if added word was the last in the list)
        new_string += '.'                   # add dot to the end
new_string = new_string.capitalize()        # make first letter of the new string capital

# adding new string to base one
# string_value = string_value[:238] + ' ' + new_string + string_value[238:len(string_value)]

substring_index = string_value.find('to the end of this paragraph.') + len('to the end of this paragraph.')
if substring_index != -1:
    string_value = string_value[:substring_index] + ' ' + new_string + string_value[substring_index:len(string_value)]

# fixing 'iz' to 'is'
# It was not specified to fix missing space in 'fix"iz"'
string_value = string_value.replace(' iz ', ' is ')


# calculating whitespaces in the string - it's 96 (instead of 87 as in task), I suppose issue is in the provided sting
# value and tab's instead of double spaces
for x in range(len(string_value)):
    if string_value[x].isspace():       # if selected element is whitespace ( ' ', '\n', '\t', '\f', '\r', '\v')
        counter += 1                    # increase counter for 1

print(string_value)                     # print to the console changed version of the text
print("Number of whitespace characters in this text = ", counter)     # print to the console counter of the whitespaces
