# .py -> bytecode -> PVM (not converted to machine code)

# variables (datatype is inferred)
age = 23 # int
name = "Tayyab" # str
price = 19.99 # float
is_student = True # bool

# type casting
price = int(price) # convert float to int

# conditionals
if condition:
    # do something
elif another_condition: # else if
    # do something else
else:
    # fallback case

# functions
def greet(name):
    print(name)

greet("Tayyab")

# data structures
list = [1, 2, 3] # ordered, mutable (editable) collection
list.append(4) # add to list
list.remove(2) # remove from list
list.pop() # remove last item
list.extend([5, 6]) # add multiple items
list.sort() # sort list
copy_list = list.copy() # copy list
list.clear() # clear list

tuple = (1, 2, 3) # ordered, immutable (uneditable) collection
list = list(tuple) # convert tuple to list
# can convert tuple to list, edit, then convert back to tuple

set = {1, 2, 3} # unordered, unique, mutable
set.add(4) # add to set
set.update([5, 6]) # add multiple items to set
set.remove(2) # remove 2 from set (2 is not the index value here), error if not found
set.discard(3) # remove 3 from set, no error if not found
set.pop() # remove random item
set.clear() # clear set

dict = {"key1": "value1", "key2": "value2"} # key-value pairs, mutable
dict["key3"] = "value3" # add new key-value pair
dict.pop("key1") # remove key1
dict.update({"key4": "value4"}) # add multiple key-value pairs
dict_keys = dict.keys() # get keys
dict_values = dict.values() # get values
dict_items = dict.items() # get key-value pairs

# loops
x = 0
while x < 5: # while loop
    print(x)
    if x == 2:
        break

for i in list:
    print(i) # for loop
    if i == 2:
        continue # skip to next iteration

for i in range(5): # range(start, stop, step)
    print(i) # prints 0 to 4

# iterators
iterator = iter(list) # create iterator from list
next_item = next(iterator) # get next item from iterator
for item in iterator: # iterate through remaining items
    print(item) # prints remaining items in the list

# generators
def generator():
    for i in range(500000000):
        yield i

gen = generator() # create generator
print(next(gen)) # 0

# As far as I understand, generators are like iterators but they are more memory efficient
# They yield one item at a time instead of storing all items in memory
# Used in case of large datasets but you don't need all items at once
# Example: reading a large file line by line
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # yield each line without newline character

# list comprehensions
s = [x for x in range(10)]  # create a list of numbers from 0 to 9
s = [x**2 for x in range(10)]  # create a list of squares of numbers from 0 to 9
s = [x for x in range(10) if x % 2 == 0]  # create a list of even numbers from 0 to 9

# error handling
try:
    result = 10 / 0  # this will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)

try:
    with open("non_existent_file.txt", "r") as file:  # this will raise a FileNotFoundError
        content = file.read()
except FileNotFoundError as e:
    print("File not found:", e)