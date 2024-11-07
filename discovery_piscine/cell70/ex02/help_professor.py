#!/usr/bin/env python3

def average(class_scores):
    return sum(class_scores.values()) / len(class_scores)

# Define the dictionaries for each class
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# Calculate and print the average for each class
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
