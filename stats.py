def word_count(text):
    full_text = text.split()
    word_count = 0
    for i in full_text:
        word_count += 1
    return word_count

def character_count(text):
    character_count = {}
    for i in text:
        if i.lower() not in character_count:
            character_count[i.lower()] = 1
        else:
            character_count[i.lower()] += 1
    return character_count

def sort_key(dictionary):
    return dictionary["num"]

def sort_dictionary(dictionary):
    sorted_list = []
    for i in dictionary:
        empty_dictionary = {}
        empty_dictionary["char"] = i
        empty_dictionary["num"] = dictionary[i]
        sorted_list.append(empty_dictionary)
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list