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

# Function to normalize given string
def string_normalizing(current_string: str) -> str:
    flag = False        # initialization of the flag
    current_string = current_string.lower().capitalize()        # making provided string lowercased and capitalized
    for x in range(len(current_string) - 2):                    # loop to go threw current string
        if flag and current_string[x].isalpha():                # if flag is true and selected letter is alphabetic
            # changing case of selected char
            current_string = current_string[0:x] + current_string[x].swapcase() + current_string[
                                                                          x + 1: len(current_string)]
            flag = False        # changing flag value
        if current_string[x] in ['.', '\n', '\t']:      # if observed char is dot, new string or tabulation
            flag = True         # changing flag value
    return current_string       # returning changed string


# Function to get last words of all sentences in provided string
def get_last_words_of_the_sentences(current_string: str) -> list:
    list_of_the_last_words = []     # initialization of the list to keep last words
    split_string = current_string.split()   # split provided string for words

    for x in range(len(split_string)):      # loop to go threw all words
        if split_string[x][len(split_string[x]) - 1] == '.':  # check if split word contains dot at the end
            list_of_the_last_words.append(split_string[x][:len(split_string[x]) - 1]) # adding word to list without dot

    return list_of_the_last_words       # return list of the last words in the text


# Function to create sentence from the last words in the text
def create_sentence_of_the_last_words(current_string: str) -> str:
    list_of_the_last_words = get_last_words_of_the_sentences(current_string)    # initialization list variable with
    # last words of the provided string
    sentence = ''       # initialization of the empty string
    for x in range(len(list_of_the_last_words)):        # loop to go threw list of the last words
        sentence += list_of_the_last_words[x]  # adding word to new string
        if x != (len(list_of_the_last_words) - 1):  # if added word was not last in list
            sentence += ' '  # add space after added word
        else:  # else (if added word was the last in the list)
            sentence += '.'     # adding dot to the end of the string
    sentence = sentence.capitalize()    # capitalize created sentence
    return sentence             # return created sentence


# Function to get end position of the substring in the provided string
def get_end_position_of_the_substring_in_the_string(substring: str, string:str) -> int:
    substring_index = string.find(substring) + len(substring)
    return substring_index


# Function to add the substring to the string
def add_substring_to_the_string(current_string: str) -> str:
    position = get_end_position_of_the_substring_in_the_string('to the end of this paragraph.', current_string)
    # return string with inserted substring
    return current_string[:position] + ' ' + create_sentence_of_the_last_words(current_string) + current_string[
                                                                                                 position:len(
                                                                                                     string_value)]


# Function to fix string
def fix_substring_in_string(current_string: str, initial_substring='iz', correct_substring='is') -> str:
    # return the string with replacements of provided substrings
    return current_string.replace(initial_substring, correct_substring)


# function to calculate the whitespaces in provided string
def calculating_whitespaces(current_string: str) -> int:
    counter = 0     # initialization of the counter
    for char in current_string:     # loop to go threw all the chars in provided string
        if char.isspace():      # if char is a whitespace
            counter += 1        # increase the counter
    return counter              # return the counter


string_value = """  
homEwork:
    tHis iz your homeWork, copy these Text to variable.

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

"""


# function to reformat provided text
def reformat_the_text(initial_string: str) -> str:
    reformatted_string = string_normalizing(initial_string)     # calling string_normalizing function to normalize text
    reformatted_string = add_substring_to_the_string(reformatted_string)  # calling function to add substring from the
    # last words
    reformatted_string = fix_substring_in_string(reformatted_string, 'iz', 'is')  # calling function to fix iz to is

    return reformatted_string       # return reformatted text


print(reformat_the_text(string_value))
# print to the console counter of the whitespaces for modified string
print("Number of whitespace characters in modified text = ", calculating_whitespaces(reformat_the_text(string_value)))

