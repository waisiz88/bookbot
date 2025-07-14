def get_num_words(file_contents): #function to get the number of words in the file
    return len(file_contents.split()) #return the number of words in the file

def get_char_frequency(file_contents): #function to get the frequency of each character in the file
    file_contents = file_contents.lower() #convert to lowercase
    my_clean_text = [c for c in file_contents if c.isalpha() or c in "æâêëô"] #create a list of characters
    my_dict = {} #create a dictionary to store the frequency of each character
    for i in my_clean_text: #iterate through the list of characters
        my_dict[i] = my_dict.get(i, 0) + 1 #add the character to the dictionary and increment the frequency
    return my_dict #return the dictionary

def get_sorted_char_counts(char_dict): #function to get the sorted character counts
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list