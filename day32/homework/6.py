# Task 1: Modify a list
def modify_list():
    my_list = [10, 20, 30, 40, 50]  # Create a list with 5 elements
    my_list.pop(2)  # Remove the 3rd element (index 2)
    my_list.insert(0, 99)  # Add a new element at index 0
    return my_list

# Task 2: Raise a number to the power of another
def power_of(a, b):
    return a ** b

# Task 3: Check if the length of a list is even or odd
def check_list_length(lst):
    if len(lst) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"

# Example Usage

# Task 1
modified_list = modify_list()
print("Modified List:", modified_list)

# Task 2
result = power_of(2, 3)  # Example: 2 raised to the power of 3
print("Power Result:", result)

# Task 3
length_check = check_list_length([1, 2, 3, 4])  # Example list
print("List Length Check:", length_check)




