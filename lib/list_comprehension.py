#!/usr/bin/env python3

def return_evens(num_list):
    return [num  for num in num_list if num % 2 ==0]
print(return_evens in range (1,10))


def make_exclamation(sentence_list):
    return [s + "!" for s in sentence_list]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

print("This Test was very tough!")
print("But guess who is tougher")

# squared_minus_one = list()
# for n in range (1, 11):
#    squared_minus_one.append((n**2)-1)
   

# print(("\n"),squared_minus_one)
# for list in squared_minus_one:
#     print(list)


# squared_minus_one = [(n**2)-1 for n in range (1, 11)]

# print(squared_minus_one)