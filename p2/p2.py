# Jordan Streete, 04/08/2021
"""
Coding Task #2 - Develop a simple Linux or Windows CLI application that sorts the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console.

NOTES:
    - I opted not to use any functions or classes because the complexity of the problem wasn't too high, so just writing it out as a script would be the simplest way to it
    - No input stop condition was provided in the question, so I just bound it to an input of 'STOP'
    - While the question did say the age and height were provided as numbers, it didn't necessarily say that they needed to be stored as ints. In addition to that, they are stored as strings in the example output, so I opted to go with that. Storing as ints is definitely doable, as I showed on lines 29-30.
"""

import operator

tuple_list = []
print("Enter your tuples, then type STOP to stop")

while True:
    # Repeatedly get input, break if input == STOP
    inp = input("tup: ")
    if inp == "STOP":
        break

    # Splits input into a list (uses comma as delimiter), and turns the list into a tuple. Finally, append the tuple to tuple_list
    formatted_input = tuple(inp.split(","))
    tuple_list.append(formatted_input)

    # If you wanted to store age and score/height as ints, you could do it like this (would replace lines 25 and 26):
    # formatted_input = inp.split(',')
    # tuple_list.append(tuple(formatted_input[0], int(formatted_input[1]), int(formatted_input[2])))

# Sort and print tuple_list
tuple_list.sort(key=operator.itemgetter(0, 1, 2))
print(tuple_list)
