from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def word_count(file: str):
    nums_word = file.split()
    return f"Found {len(nums_word)} total words"

def count_char(file)-> dict[str, int]:
    char_count = {}
    lowercase_char = file.lower()

    for char in lowercase_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def char_count_list(count_dict)-> list[CharacterCount]:
    char_list = []
    
    for char in count_dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = count_dict[char]
        char_list.append(new_dict)
        
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list