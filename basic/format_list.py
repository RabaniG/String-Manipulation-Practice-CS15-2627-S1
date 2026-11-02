string_to_process = "eggs,cheese,milk,bread,cereal"

items = string_to_process.strip().split(",")
uppercase_items = []

for item in items:
    # upper case each item
    uppercase_items.append(item.upper())

print(" | ".join(uppercase_items))