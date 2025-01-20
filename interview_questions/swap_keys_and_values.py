from typing import Dict, Union, List

dictionary={1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'a', 6: 'e'}

def reverse_keys_and_values(
    dictionary: Dict[int,str]
) ->Dict[str,Union[List,int]]:
    returned_dict = {}
    for key, value in dictionary.items():
        if value in returned_dict:
            if isinstance(returned_dict[value], list):
                returned_dict[value].append(key)
            else:
                prev = returned_dict[value]
                returned_dict[value]=[prev, key]
        else:
            returned_dict[value] = key
    return returned_dict

print(reverse_keys_and_values(dictionary))