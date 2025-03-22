from collections import OrderedDict

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def sort_dict(dictionary):
    return OrderedDict(sorted(dictionary.items()))

def get_characters_dict(text):
    text = text.lower()
    characters_dict = {}
    for i in range(0, len(text)):
        char = text[i]
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
 
    return characters_dict