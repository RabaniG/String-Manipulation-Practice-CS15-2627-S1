string_to_process = "  18,27,35,20  "

# Remove whitespace and split the string into individual number strings
number_strings = string_to_process.strip()
number_strings = number_strings.split(",")

numbers = []

# Convert each number string to an integer
for number_string in number_strings:
    numbers.append(int(number_string))

total = sum(numbers)
average = total / len(numbers)

# Output
print("Total:", total)
print("Average:", average)
