#!/usr/bin/env python3

def find_the_redheads(persons):
    list = []
    key = "red"
    for key in persons.keys():
        list.append(key)
        return list

persons = {
"florian": "red",
"marie": "blond",
"virgine": "brunette",
"david": "red"
}

print(find_the_redheads(persons))
# for first_name, last_name in persons.items():
#     array_of_name(first_name,last_name)
