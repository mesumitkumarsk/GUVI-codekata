def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Input handling
def input_dictionary():
    input_str = input()
    return eval(input_str)

dict1 = input_dictionary()
dict2 = input_dictionary()

print(merge_dictionaries(dict1, dict2))