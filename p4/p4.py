"""
Coding Task #4- Develop a simple Linux or Windows CLI application that computes the frequency of the words from the input. The output should output after sorting the key alphanumerically.

NOTES:
    - While comprehensions can sacrifice readability for succinctness, I felt that this dictionary comprehension was simple enough to use 
    - While I don't necessarily need to cast the sorted frequency_dict list back into a dictionary, it felt weird leaving it as a list
    - Using OrderedDict would've been unnecessary, as normal python dicts now remeber intertion order anyway
"""

# Get input and split at each space
inp = input().split(" ")

# Dictionary comprehension that takes each word as key and its count within the sentence as value. Dict is unordered at this point.
frequency_dict = {word: inp.count(word) for word in inp}

# Sort the dict by key using sorted. items() turns the data structure into (basically) a list of tuples, so we cast it as dict to bring it back to a dictionary
ordered_freq_dict = dict(sorted(frequency_dict.items()))

# Print each item of the sorted dictionary
for k, v in ordered_freq_dict.items():
    print(f"{k}:{v}")
