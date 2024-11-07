#!/usr/bin/env python3

def array_of_name(first_name,last_name):
    whole_name = first_name.capitalize() + " " + last_name.capitalize()
    print(whole_name)

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
for first_name, last_name in persons.items():
    array_of_name(first_name,last_name)
